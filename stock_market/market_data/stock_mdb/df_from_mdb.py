import market_data as md
import pandas as pd
from datetime import datetime

from bson import json_util
from pandas import json_normalize
import json

from pymongo import MongoClient
client = MongoClient()
db = client[md.db_client]

def get_df_from_mdb_for_nday(ndays, coll_name, symbols='', incl='', dateidx=True):
    db_coll = db[coll_name]
    adate = md.get_date_for_mdb(ndays)
    df = pd.DataFrame({})
    if len(incl) != 0:
        symbols = md.get_symbols(incl)
    if db_coll.count_documents({'Date': adate}) > 0:
        if len(symbols) > 0:
            symbols.append('Date')  # Date field to be included in mdb results
            mdb_data = db_coll.find({'Date': adate},symbols)
            symbols.remove('Date')
        else:
            mdb_data = db_coll.find({'Date': adate})
        df = md.mdb_to_df(mdb_data, dateidx)
    #print('mdb records {} for {} symbols on {}'.format(df.size,len(symbols),adate),end=', ')
    return df


def get_df_from_mdb(ndays,db_coll_name,columns='',query_field='Date'):
    adate = md.get_date_for_mdb(ndays)
    db_coll = db[db_coll_name]
    if len(columns) == 0:
        mdb_data = db_coll.find({query_field: adate})
    else:
        mdb_data = db_coll.find({query_field: adate},columns)
    df = md.mdb_to_df(mdb_data)
    return df



def get_df_from_mdb_between_days(ndays_ago, dbcol_name, symbols='', incl=md.all, start=0):
    db_coll = db[dbcol_name]
    start_date = md.get_date_for_mdb(ndays_ago)
    if not 'Date' in symbols:
        symbols.append('Date')
    df = pd.DataFrame({})
    if start==0:
        mdb_data = db_coll.find({'Date': {'$gte':start_date}},symbols)
    else:
        end_date = md.get_date_for_mdb(ndays_to)
        mdb_data = db_coll.find({'Date': {'$lte':end_date, '$gte':start_date}},symbols)
    df = md.mdb_to_df(mdb_data, dateidx=True)
    return df

#
# def get_mdb_row_for_date(adate, db_coll_name, addtodb='False'):
#     db_coll = db[db_coll_name]
#     df = pd.DataFrame({})
#     try:
#         mdb_data = db_coll.find({db_coll : adate})
#         df = md.mdb_to_df(mdb_data, dateidx=True)
#     except:
#         import sys
#         e = sys.exc_info()
#         print(e)
#         print('{} mdb index error - no records for {}.'.format(db_coll_name, adate))
#         if addtodb == True:
#             ndays = md.getNBusDaysFromDateStr(adate.strftime("%Y-%m-%d"))
#             df = md.get_yahoo_ndays_ago(ndays, md.get_symbols(directory=md.all))
#             df = df.dropna(axis=1, how='all')
#             md.addCloseVolumeRowToMdb(df,db_coll)
#             mdb_data = db_coll.find({db_coll: adate})
#             df = md.mdb_to_df(mdb_data, dateidx=True)
#     return df


### SYMBOL queries

def get_df_from_mdb_columns(columns, db_colln):
    columns.append('Date')
    db_coll = db[db_colln]
    mdb_data= db_coll.find({}, columns)
    df = md.mdb_to_df(mdb_data, dateidx=True)
    return df


## REDUNDANT


def get_df_mdb_nrows_step(start,days_step, coll_name,symbols='', incl=md.all):
    days,step = days_step[0],days_step[1]
    dfa = pd.DataFrame(columns=['Date'])
    for ndays in range(start,start+days,step):
        df = get_df_from_mdb_for_nday(ndays, coll_name, symbols)
        df = df.reset_index().rename(columns={'index':'Date'})
        dfa = pd.concat([dfa,df])
    dfa.sort_values(by=['Date'], ascending=[True], inplace=True)
    return dfa


def mdb_document_count(ndays, db_coll_name):
    adate = md.get_date_for_mdb(ndays)
    db_coll = db[db_coll_name]
    return db_coll.count_documents({'Date': adate})
