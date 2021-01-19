from datetime import datetime
import numpy as np
import pandas as pd
import calendar
import trading_calendars as tc
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

def getNDateAndToday(ndays):
    end = getNBusDateFromNdays(0)
    start = getNBusDateFromNdays(ndays)
    return start,end
