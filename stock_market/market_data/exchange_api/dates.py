from datetime import datetime
import numpy as np
import pandas as pd
import pandas_market_calendars as mcal

cme = mcal.get_calendar("NYSE")

def get_busdate_ndays_ago(ndays):
    strdate = '{:%Y-%m-%d}'.format(datetime.now())
    dt = np.busday_offset(dates=strdate, offsets=-ndays, roll='backward', holidays=cme.holidays().holidays)
    return str(dt)

def get_nbusdays_from_datestr(prev_date):
    dtnow = '{:%Y-%m-%d}'.format(datetime.now())
    bus_dtnow = np.busday_offset(dates=dtnow, offsets=0, roll='backward',holidays=cme.holidays().holidays)
    dt = str(bus_dtnow)
    nbdays =  np.busday_count(prev_date, dt,holidays=cme.holidays().holidays)
    return nbdays

def get_desc_date(dfRow):
    date = pd.to_datetime(dfRow.index.values[0])
    return calendar.day_name[date.weekday()]+' '+'{:%Y-%m-%d}'.format(date)


def get_dates_ndays_and_today(ndays):
    t0day = get_busdate_ndays_ago(0)
    nday = get_busdate_ndays_ago(ndays)
    return nday,t0day


def get_ndate_and_prevdate(ndays, step):
    pday = get_busdate_ndays_ago(ndays + step)
    day = get_busdate_ndays_ago(ndays)
    return pday,day




