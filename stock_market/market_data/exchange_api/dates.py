import numpy as np
import pandas as pd
import pandas_market_calendars as mcal
from datetime import datetime
from dateutil.relativedelta import relativedelta
cme = mcal.get_calendar("NYSE")

def get_busdate_ndays_ago(ndays):
    strdate = '{:%Y-%m-%d}'.format(datetime.now())
    dt = np.busday_offset(dates=strdate, offsets=-ndays, roll='backward', holidays=cme.holidays().holidays)
    return str(dt)


def get_nbusdays_from_datestr(datestr):
    dtnow = '{:%Y-%m-%d}'.format(datetime.now())
    bus_dtnow = np.busday_offset(dates=dtnow, offsets=0, roll='backward',holidays=cme.holidays().holidays)
    dt = str(bus_dtnow)
    nbdays =  np.busday_count(datestr, dt, holidays=cme.holidays().holidays)
    return nbdays


def get_nbusdays_from_date(date):
    datestr = f'{date:%Y-%m-%d}'
    dtnow = '{:%Y-%m-%d}'.format(datetime.now())
    bus_dtnow = np.busday_offset(dates=dtnow, offsets=0, roll='backward',holidays=cme.holidays().holidays)
    dt = str(bus_dtnow)
    nbdays =  np.busday_count(datestr, dt, holidays=cme.holidays().holidays)
    return nbdays

def get_ndays_range_wfm3612(end = 1):
    now = datetime.now()
    yr1 = get_nbusdays_from_date(now - relativedelta(years=1))
    mnth6 = get_nbusdays_from_date(now - relativedelta(months=6))
    mnth3 = get_nbusdays_from_date(now - relativedelta(months=3))
    mnth1 = get_nbusdays_from_date(now - relativedelta(months=1))
    wks2 = get_nbusdays_from_date(now- relativedelta(weeks=2))
    wks1 = get_nbusdays_from_date(now - relativedelta(weeks=1))
    return end, wks1 + 1, wks2 + 1, mnth1 + 1, mnth3 + 1, mnth6 + 1, yr1 + 1

def get_ndays_range_montlhly(end = 1):
    now = datetime.now()
    periods = [1]
    for idx in range(end + 1, 13,2):
        periods.append(get_nbusdays_from_date(now - relativedelta(months = idx)) + 1)
    return tuple(periods)


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




