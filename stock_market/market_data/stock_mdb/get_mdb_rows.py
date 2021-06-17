import market_data as md
import pandas as pd
from datetime import datetime

from bson import json_util
from pandas import json_normalize
import json

from pymongo import MongoClient
client = MongoClient()
db = client[md.db_client]


## Date Queries

def get_df_mdb_nrows_step(start,days_step, coll_name,symbols='', incl=md.all):
    days,step = days_step[0],days_step[1]
    dfa = pd.DataFrame(columns=['Date'])
    for ndays in range(start,start+days,step):
        df = get_mdb_row(ndays, coll_name, symbols)
        df = df.reset_index().rename({'index':'Date'})
        dfa = pd.concat([dfa,df])
    dfa.sort_values(by=['Date'], ascending=[True], inplace=True)
    return dfa


def get_mdb_row(ndays, coll_name, symbols='',incl=''):
    db_coll = db[coll_name]
    adate = md.get_date_for_mdb(ndays)
    df = pd.DataFrame({})
    if len(incl) != 0:
        symbols = md.get_symbols(incl)
        symbols.append('Date')  # Date field to be included in mdb results
    elif len(symbols) > 0:
        symbols.append('Date')  # Date field to be included in mdb results
    if db_coll.count_documents({'Date': adate}) > 0:
        if len(symbols) > 0:
            mdb_data = db_coll.find({'Date': adate},symbols)
        else:
            mdb_data = db_coll.find({'Date': adate})
        df = md.mdb_to_df(mdb_data)
    return df


def get_df_mdb_rows(ndays_ago,dbcol_name,symbols='',incl=md.all,start=0):
    db_coll = db[dbcol_name]
    start_date = md.get_date_for_mdb(ndays_ago)
    df = pd.DataFrame({})
    if start==0:
        mdb_data = db_coll.find({'Date': {'$gte':start_date}},symbols)
    else:
        end_date = md.get_date_for_mdb(ndays_to)
        mdb_data = db_coll.find({'Date': {'$lte':end_date, '$gte':start_date}},symbols)
    df = md.mdb_to_df(mdb_data)
    df['Date'] = df['Date.$date'].apply(lambda x: datetime.utcfromtimestamp(float(x / 1e3)))
    df.set_index('Date', inplace=True)
    df.drop(['Date.$date', '_id.$oid'], axis=1, inplace=True)
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


def getdf_ndays_mdb_row(ndays, db_coll):
    adate = md.get_date_for_mdb(ndays)
    df = pd.DataFrame({})
    if db_coll.count_documents({'Date': adate}) > 0:
        mdb_data = db_coll.find({'Date': adate})[0]
        df = md.mdb_to_df(mdb_data)
        df['Date'] = datetime.utcfromtimestamp(float(df['Date.$date'] / 1e3))
        df.set_index('Date', inplace=True)
        df.drop(['Date.$date', '_id.$oid'], axis=1, inplace=True)
    return df

def get_mdb_row_for_date(adate, db_coll_name, addtodb='False', find_col='Date'):
    db_coll = db[db_coll_name]
    df = pd.DataFrame({})
    try:
        mdb_data = db_coll.find({find_col: adate})
        df = md.mdb_todf_with_date_index(mdb_data)
    except:
        import sys
        e = sys.exc_info()
        print(e)
        print('{} mdb index error - no records for {}.'.format(db_coll_name, adate))
        if addtodb == True:
            ndays = md.getNBusDaysFromDateStr(adate.strftime("%Y-%m-%d"))
            df = md.get_yahoo_ndays_ago(ndays, md.get_symbols(incl='ALL'))
            df = md.addCloseVolumeRowToMdb(df,db_coll)
    return df


### SYMBOL queries

def get_df_for_symbol(symbol, db_colln):
    db_coll = db[db_colln]
    mdb_data= db_coll.find({'symbol': symbol})
    df = md.mdb_to_df(mdb_data)
    df['Date'] = df['Date.$date'].apply(lambda x:datetime.utcfromtimestamp(float(x / 1e3)))
    df.set_index('Date', inplace=True)
    df.drop(['Date.$date', '_id.$oid'], axis=1, inplace=True)
    return df


