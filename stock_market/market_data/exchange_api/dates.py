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


def get_ndays_periods(months=[],weeks=[],last_day=1):
    now = datetime.now()
    periods = []
    for idx in months:
        periods.append(get_nbusdays_from_date(now - relativedelta(months=idx)))
    for idx in weeks:
        periods.append(get_nbusdays_from_date(now - relativedelta(weeks=idx)))
    periods.append(last_day)
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




