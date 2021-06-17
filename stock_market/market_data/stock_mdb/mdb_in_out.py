import market_data as md
import performance as pf
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

def add_df_to_db(df, db_coll_name, dropidx=False):
    db_coll = db[db_coll_name]
    df = df.copy(deep=True)
    df.drop_duplicates(inplace=True)
    df.reset_index(inplace=True)
    if dropidx == True:
        df.drop(columns={'index'},inplace=True)
    data_dict = df.to_dict("records")
    result = db_coll.insert_many(data_dict)
    print('Added {:d} of {:d}'.format(len(result.inserted_ids),len(df.index)))
    return result


def add_dfup_to_db(dfup, db_coll_name):
    dt = max(dfup.date.values)
    dt = md.getMdbDateFromStrDate(dt)
    df = pd.DataFrame(columns=['Date', 'symbol'])
    df['symbol'] = dfup.symbol.unique()
    df['Date'] = dt
    md.add_df_to_db(df, db_coll_name, dropidx=True)


def getMdbDateFromStrDate(strDate):
    return datetime.strptime(strDate, '%Y-%m-%d')

def get_date_for_mdb(ndays):
    strDate = md.getNBusDateFromNdays(ndays)
    return datetime.strptime(strDate, '%Y-%m-%d')


def addCloseVolumeRowToMdb(df):
    add_df_to_db(df['Close'], 'market_data_close')
    add_df_to_db(df['Volume'], 'market_data_volume')
 #   adate = df.index[0]
 #   mdb_data = db_coll.find({'Date': adate})[0]
    return df

def getMdbRowsCloseVol(strdate,incl='ALL'):
    adate = getMdbDateFromStrDate(strdate)
    dbcoll_name = 'market_data_close'
    dfClose = md.get_mdb_row_for_date(adate, dbcoll_name,addtodb=True)
    dbcoll_name = 'market_data_volume'
    dfVol = md.get_mdb_row_for_date(adate, dbcoll_name,addtodb=True)
    if incl != md.all:
        dfClose = pf.filteredbySymbols(dfClose, incl, colorrow='col')
        dfVol = pf.filteredbySymbols(dfVol, incl, colorrow='col')
    return dfClose,dfVol


def mdb_to_df(mongo_data):
    sanitized = json.loads(json_util.dumps(mongo_data))
    normalized = json_normalize(sanitized)
    df = pd.DataFrame(normalized)
    return df

def mdb_todf_with_date_index(mongo_data):
    df = mdb_to_df(mongo_data)
    df['Date'] = datetime.utcfromtimestamp(float(df['Date.$date'] / 1e3))
    df.set_index('Date', inplace=True)
    df.drop(['Date.$date', '_id.$oid'], axis=1, inplace=True)
    return df


