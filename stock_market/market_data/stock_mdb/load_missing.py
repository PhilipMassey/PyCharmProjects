import market_data as md
import pandas as pd
from datetime import datetime
from pymongo import MongoClient

import trading_calendars as tc
xnys = tc.get_calendar("XNYS")


client = MongoClient()
db = client['stock_market']


def getMissingMarketRow(ndays, db_coll, symbols):
    df = md.getNdaysRowFromMdb(ndays, db_coll)
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
        dt = md.getMdbDateFromNdays(ndays)
        query = {'Date': dt}
        result = db_coll.update_one(query, newvalues)
        print(ndays, len(data_dict[0]), result.matched_count, result.modified_count)


def updateRowWithMissing(ndays, db_coll, symbols):
    df_m = md.getMissingMarketRow(ndays, symbols)
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


