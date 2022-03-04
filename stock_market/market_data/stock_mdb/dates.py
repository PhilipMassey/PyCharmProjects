import market_data as md
import pandas as pd
import numpy as np
from datetime import datetime

def df_idxdate_tostr(df):
    d = df.index.values[0]
    return np.datetime_as_string(d, timezone='UTC')[:10]

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

def get_date_for_ndays(ndays):
    dt = get_date_for_mdb(ndays)
    return f'{dt:%b %-d}'

