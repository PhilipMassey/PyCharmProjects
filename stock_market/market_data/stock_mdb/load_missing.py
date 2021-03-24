import market_data as md
import pandas as pd
from pymongo import MongoClient

import trading_calendars as tc
xnys = tc.get_calendar("XNYS")


client = MongoClient()
db = client['stock_market']


def getMissingMarketRow(ndays, db_coll, symbols):
    dbaction = None
    df = md.getNdaysRowFromMdb(ndays, db_coll)
    if df.size == 0: #missing whole row of data, missing all symbole
        missing_symbols = md.getAllPortfoliosSymbols()
        dbaction = 'ADD'
    else:
        dfs = set(df.columns)
        missing_symbols = set(symbols).difference(dfs)
        dbaction = 'UPDATE'
    if len(missing_symbols) > 0:
        return (md.getRowNDaysAgo(ndays, missing_symbols),dbaction)
    else:
        return (pd.DataFrame({}),dbaction)


def updateMdbWithRow(ndays, df_m, db_coll):
    if df_m.size > 1:
        df_mc = df_m.copy(deep=True)
        df_mc = df_mc.dropna(axis='columns')
        df_mc.reset_index(inplace=True)
        df_mc.drop(columns=['Date'], inplace=True)
        data_dict = df_mc.to_dict("records")
        # print(data_dict)
        newvalues = {"$set": data_dict[0]}
        dt = md.getMdbDateFromNdays(ndays)
        query = {'Date': dt}
        result = db_coll.update_one(query, newvalues)
        print(ndays, len(data_dict[0]), result.matched_count, result.modified_count)


def updateMdbWithMissingRow(ndays, symbols):
    start, end = md.getNDateAndToday(ndays)
    print(ndays,start,end)
    db_coll = db["market_data_close"]
    df_m,dbaction = getMissingMarketRow(ndays, db_coll, symbols)
    if df_m.size > 0:
        if dbaction == 'ADD':
            md.addCloseVolumeRowToMdb(df_m,db_coll)
        else:
            updateMdbWithRow(ndays, df_m['Close'], db_coll)
            db_coll = db["market_data_volume"]
            updateMdbWithRow(ndays, df_m['Volume'], db_coll)


#
# def updateRowWithMissing(ndays, db_coll, symbols):
#     df_m = md.getMissingMarketRow(ndays, symbols)
#     updateMdbWithRow(df_m, db_coll)
#
