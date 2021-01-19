import market_data as md
import pandas as pd
from pymongo import MongoClient
from datetime import datetime
import trading_calendars as tc
xnys = tc.get_calendar("XNYS")


client = MongoClient()
db = client['stock_market']

def getMdbDateFromStrDate(strDate):
    return datetime.strptime(strDate, '%Y-%m-%d')

def getMdbDateFromNdays(ndays):
    strDate = md.getNBusDateFromNdays(ndays)
    return datetime.strptime(strDate,'%Y-%m-%d')

def addRowToMdb(df,db_coll):
    df = md.removeBadData(df)
    df.reset_index(inplace=True)
    data_dict = df.to_dict("records")
    result = db_coll.insert_many(data_dict)
    print(len(result.inserted_ids))
    return result.inserted_ids

def getMdbRowForDate(adate,db_coll):
    try:
        mdb_data = db_coll.find({'Date': adate})[0]
    except:
        print('index error',adate)
        ndays = md.getNBusDaysFromDateStr(adate.strftime("%Y-%m-%d"))
        df = md.getRowNDaysAgo(ndays,md.getPortfoliosSymbols())
        addRowToMdb(df['Close'],db['market_data_close'])
        addRowToMdb(df['Volume'],db['market_data_volume'])
        mdb_data = db_coll.find({'Date': adate})[0]
    return md.MdbToDataframe(mdb_data)


def getMdbRowsCloseVol(strdate):
    adate = getMdbDateFromStrDate(strdate)
    db_coll = db['market_data_close']
    dfClose = getMdbRowForDate(adate,db_coll)
    db_coll = db['market_data_volume']
    dfVol = getMdbRowForDate(adate,db_coll)
    return dfClose,dfVol

def strdfidxDate(df):
    dt = df.index.values[0]
    return pd.to_datetime(str(dt)) .strftime('%Y-%m-%d')

