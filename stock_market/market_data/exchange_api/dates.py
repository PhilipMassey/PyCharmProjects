from datetime import datetime
import numpy as np
import pandas as pd
import calendar
import trading_calendars as tc
import warnings
import math
warnings.simplefilter(action='ignore', category=FutureWarning)
xnys = tc.get_calendar("XNYS")

def getNBusDaysFromDateStr(ymd_date):
    dtnow = '{:%Y-%m-%d}'.format(datetime.now())
    bdtnow = np.busday_offset(dtnow, 0, roll='backward')
    dt = str(bdtnow)
    nbdays =  np.busday_count(ymd_date, dt)
    return nbdays

def getDescriptiveDate(dfRow):
    date = pd.to_datetime(dfRow.index.values[0])
    return calendar.day_name[date.weekday()]+' '+'{:%Y-%m-%d}'.format(date)

def getRowYmdDate(dfRow):
    rowdate =  pd.to_datetime(dfRow.index.values[0])
    return '{:%Y-%m-%d}'.format(rowdate)

def getNBusDateFromNdays(ndays,skip=False):
    if ndays == 0:
        dtnow = '{:%Y-%m-%d}'.format(datetime.now())
        dt = np.busday_offset(dtnow, 0, roll='backward')
        if not xnys.is_session(dt):
            return getNBusDateFromNdays(ndays + 1,skip)
    else:
        now = '{:%Y-%m-%d}'.format(datetime.now())
        dtnow = np.busday_offset(now,0,roll='backward')
        dt = np.busday_offset(dtnow,-ndays,roll='backward')
        if not xnys.is_session(dt):
            if skip:
                dt = str('SKIP')
            else:
                return getNBusDateFromNdays(ndays + 1,skip)
        #print('ndays {:d} bdate {}'.format(ndays,dt))
    return str(dt)

def get_dates_ndays_and_today(ndays):
    t0day = getNBusDateFromNdays(0)
    nday = getNBusDateFromNdays(ndays)
    return nday,t0day


def getNDateAndPrevDate(ndays,step):
    pday = getNBusDateFromNdays(ndays+step)
    day = getNBusDateFromNdays(ndays)
    return pday,day

def get_ndays_to(strdate='2020-04-01'):
    """
    :parmam default: trading day for 2020 bottom
    :return: ndays from
    """
    ndays = getNBusDaysFromDateStr(strdate)
    return ndays


def get_period_interval(ndays=0):
    """
        :Defaults to trading ndays from 2020 bottom
        :return:
        """

    if ndays == 0:
        ndays = get_ndays_to()
    steps = 10
    step = ndays/steps
    if step < 1:
        step = 1
    return ndays,math.floor(step)
    # nweeks = int(ndays/5)
    # nmonths = int(ndays/20)-1
    # start,end = getNDateAndToday(ndays)
    # print('ndays ',ndays,start,end,' nmonths ',nmonths,' nweeks ',nweeks)
    # if nmonths > 6:
    #     step = nmonths
    # elif nweeks > 20:
    #     step = nweeks
    # else:
    #     step = 1
    # return ndays,step




