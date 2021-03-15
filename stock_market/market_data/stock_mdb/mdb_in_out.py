import market_data as md
import pandas as pd
from datetime import datetime
import trading_calendars as tc
xnys = tc.get_calendar("XNYS")
from pymongo import MongoClient
from bson import json_util
from pandas import json_normalize
import json

client = MongoClient()
db = client['stock_market']

def strdfidxDate(df):
    dt = df.index.values[0]
    return pd.to_datetime(str(dt)) .strftime('%Y-%m-%d')

def addRowToMdb(df,db_coll):
    data_dict = df.to_dict("records")
    result = db_coll.insert_many(data_dict)
    print(len(result.inserted_ids))
    return result

def getMdbDateFromStrDate(strDate):
    return datetime.strptime(strDate, '%Y-%m-%d')

def getMdbDateFromNdays(ndays):
    strDate = md.getNBusDateFromNdays(ndays)
    return datetime.strptime(strDate,'%Y-%m-%d')

def getMdbDateFromNdays(ndays):
    strDate = md.getNBusDateFromNdays(ndays)
    return datetime.strptime(strDate, '%Y-%m-%d')

def getMdbRowForDate(adate,db_coll):
    try:
        mdb_data = db_coll.find({'Date': adate})[0]
    except:
        print('index error',adate)
        ndays = md.getNBusDaysFromDateStr(adate.strftime("%Y-%m-%d"))
        df = md.getRowNDaysAgo(ndays, md.getAllPortfoliosSymbols())
        addRowToMdb(df['Close'],db['market_data_close'])
        addRowToMdb(df['Volume'],db['market_data_volume'])
        mdb_data = db_coll.find({'Date': adate})[0]
    return md.MdbToDataframeForPercent(mdb_data)


def getMdbRowsCloseVol(strdate):
    adate = getMdbDateFromStrDate(strdate)
    db_coll = db['market_data_close']
    dfClose = getMdbRowForDate(adate,db_coll)
    db_coll = db['market_data_volume']
    dfVol = getMdbRowForDate(adate,db_coll)
    return dfClose,dfVol


def MdbToDataframe(mongo_data):
    sanitized = json.loads(json_util.dumps(mongo_data))
    normalized = json_normalize(sanitized)
    df = pd.DataFrame(normalized)
    return df

def MdbToDataframeForPercent(mongo_data):
    df = MdbToDataframe(mongo_data)
    df['Date'] = datetime.utcfromtimestamp(float(df['Date.$date'] / 1e3))
    df.set_index('Date', inplace=True)
    df.drop(['Date.$date', '_id.$oid'], axis=1, inplace=True)
    return df

def getNdaysRowFromMdb(ndays, db_coll):
    adate = getMdbDateFromNdays(ndays)
    mdb_data = db_coll.find({'Date': adate})[0]
    df = MdbToDataframe(mdb_data)
    df['Date'] = datetime.utcfromtimestamp(float(df['Date.$date'] / 1e3))
    df.set_index('Date', inplace=True)
    df.drop(['Date.$date', '_id.$oid'], axis=1, inplace=True)
    return df

