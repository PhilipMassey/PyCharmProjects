import market_data as md
import pandas as pd
from datetime import datetime

def df_idxdate_tostr(df):
    return df.index.values[0].strftime('%Y-%m-%d')

def df_idxdate_to_mdbdate(df):
    ts = df.index.values[0]
    dt= pd.to_datetime(str(ts))
    timestring = dt.strftime('%Y-%m-%d')
    return get_mdbdate_from_strdate(timestring)

def get_mdbdate_from_strdate(strDate):
    return datetime.strptime(strDate, '%Y-%m-%d')

def get_date_for_mdb(ndays):
    strDate = md.get_busdate_ndays_ago(ndays)
    return datetime.strptime(strDate, '%Y-%m-%d')
