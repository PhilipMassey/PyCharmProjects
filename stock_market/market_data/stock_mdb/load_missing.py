import market_data as md
import pandas as pd
from pymongo import MongoClient

import trading_calendars as tc
xnys = tc.get_calendar("XNYS")


client = MongoClient()
db = client['stock_market']


def get_missing_market_row(ndays, symbols):
    dbaction = None
    db_coll_name = md.db_close
    df = md.get_df_from_mdb(ndays, db_coll_name)
    if df.size == 0: #missing whole row of data, missing all symbole
        missing_symbols = md.get_symbols(incl=md.all)
        dbaction = 'ADD'
    else:
        dfs = set(df.columns)
        missing_symbols = set(symbols).difference(dfs)
        dbaction = 'UPDATE'
    if len(missing_symbols) > 0:
        return (md.get_yahoo_ndays_ago(ndays, missing_symbols), dbaction)
    else:
        return (pd.DataFrame({}),dbaction)


def update_mdb_with_dfrow(ndays, df_m, coll_name):
    db_coll = db[coll_name]
    if df_m.size > 1:
        df_mc = df_m.copy(deep=True)
        df_mc = df_mc.dropna(axis='columns')
        df_mc.reset_index(inplace=True)
        df_mc.drop(columns=['Date'], inplace=True)
        data_dict = df_mc.to_dict("records")
        # print(data_dict)
        newvalues = {"$set": data_dict[0]}
        dt = md.get_date_for_mdb(ndays)
        query = {'Date': dt}
        result = db_coll.update_one(query, newvalues)
        #print(ndays, len(data_dict[0]), result.matched_count, result.modified_count)


def update_mdb_with_missing_row(ndays, symbols):
    start, end = md.get_dates_ndays_and_today(ndays)
    print(ndays,start,end)
    df_m,dbaction = get_missing_market_row(ndays, symbols)
    if df_m.size > 0:
        if dbaction == 'ADD':
            md.addCloseVolumeRowToMdb(df_m)
        else:
            update_mdb_with_dfrow(ndays, df_m['Close'], md.db_close)
            db_coll = db["market_data_volume"]
            update_mdb_with_dfrow(ndays, df_m['Volume'], md.db_vol)


#
# def updateRowWithMissing(ndays, db_coll, symbols):
#     df_m = md.getMissingMarketRow(ndays, symbols)
#     updateMdbWithRow(df_m, db_coll)
#
