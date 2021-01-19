import sys

sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])

import market_data as md
import pandas as pd
from datetime import datetime

from pymongo import MongoClient
from bson import json_util, ObjectId
from pandas import json_normalize
import json

client = MongoClient()
db = client['stock_market']


def removeBadData(df):
    if 'BRK.B' in list(df.columns):
        print(df['BRK.B'])
        return df.drop(columns=['BRK.B'])
    return df


def addPicklesToMdbConn(ndays):
    print(ndays)
    dfall = md.getStockPickleNBDays(ndays, skip=True)
    if dfall.size > 0:
        df = dfall['Close']
        df = removeBadData(df)
        df.reset_index(inplace=True)
        data_dict = df.to_dict("records")
        db["market_data_close"].insert_many(data_dict)
        df = dfall['Volume']
        df = removeBadData(df)
        df.reset_index(inplace=True)
        data_dict = df.to_dict("records")
        db["market_data_volume"].insert_many(data_dict)


def getMdbDateFromNdays(ndays):
    strDate = md.getNBusDateFromNdays(ndays)
    return datetime.strptime(strDate, '%Y-%m-%d')


def MdbToDataframe(mongo_data):
    sanitized = json.loads(json_util.dumps(mongo_data))
    normalized = json_normalize(sanitized)
    df = pd.DataFrame(normalized)
    df['Date'] = datetime.utcfromtimestamp(float(df['Date.$date'] / 1e3))
    df.set_index('Date', inplace=True)
    df.drop(['Date.$date', '_id.$oid'], axis=1, inplace=True)
    return df


def getNdaysRowFromMdb(ndays, db_coll):
    adate = getMdbDateFromNdays(ndays)
    mdb_data = db_coll.find({'Date': adate})[0]
    return MdbToDataframe(mdb_data)


def getMissingMarketRow(ndays, db_coll, symbols):
    df = getNdaysRowFromMdb(ndays, db_coll)
    dfs = set(df.columns)
    missing_symbols = set(symbols).difference(dfs)
    if len(missing_symbols) > 0:
        return md.getRowNDaysAgo(ndays, missing_symbols)
    else:
        return pd.DataFrame({})


def updateMdbWithRow(ndays, df_m, db_coll):
    if df_m.size > 1:
        df_m = df_m.dropna(axis='columns')
        df_m.reset_index(inplace=True)
        df_m.drop(columns=['Date'], inplace=True)
        data_dict = df_m.to_dict("records")
        # print(data_dict)
        newvalues = {"$set": data_dict[0]}
        dt = getMdbDateFromNdays(ndays)
        query = {'Date': dt}
        result = db_coll.update_one(query, newvalues)
        #print(ndays, len(data_dict[0]), result.matched_count, result.modified_count)


def updateRowWithMissing(ndays, db_coll, symbols):
    df_m = getMissingMarketRow(ndays, symbols)
    updateMdbWithRow(df_m, db_coll)


def updateMdbWithMissingRow(ndays, symbols):
    print(ndays)
    db_coll = db["market_data_close"]
    df_m = getMissingMarketRow(ndays, db_coll, symbols)
    if df_m.size > 0:
        updateMdbWithRow(ndays, df_m['Close'], db_coll)
        db_coll = db["market_data_volume"]
        # df_m = getMissingMarketRow(ndays,df_col)
        updateMdbWithRow(ndays, df_m['Volume'], db_coll)



