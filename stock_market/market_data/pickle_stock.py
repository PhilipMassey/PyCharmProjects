import market_data as md
import numpy as np
import pandas as pd
import yfinance as yf
import calendar
from datetime import datetime
import trading_calendars as tc
xnys = tc.get_calendar("XNYS")


def getStockPickleDirectory():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/stock_pickles'
    return path

def getPickleName(yymmdd):
    ppath = getStockPickleDirectory()
    return ppath+'/'+yymmdd+'.pk'

def getNDateAndToday(ndays):
    end = getNBusDateFromNdays(0)
    start = getNBusDateFromNdays(ndays)
    return start,end

def getNBusDateFromNdays(ndays):
    if ndays == 0:
        dtnow = '{:%Y-%m-%d}'.format(datetime.now())
        dt = np.busday_offset(dtnow, 0, roll='backward')
        if not xnys.is_session(dt):
            return getNBusDateFromNdays(ndays + 1)
    else:
        now = '{:%Y-%m-%d}'.format(datetime.now())
        dtnow = np.busday_offset(now,0,roll='backward')
        dt = np.busday_offset(dtnow,-ndays,roll='backward')
        if not xnys.is_session(dt):
            return getNBusDateFromNdays(ndays + 1)
        #print('ndays {:d} bdate {}'.format(ndays,dt))
    return str(dt)

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

def __getStockPickle(datestr):
    pk_name = getPickleName(datestr)
    return pd.read_pickle(pk_name)

def getStockPickleNBDays(ndays):
    datestr = md.getNBusDateFromNdays(ndays)
    return getStockPickle(datestr)

def getStockPickle(datestr):
    try:
        dfNDaysAgo = __getStockPickle(datestr)
    except FileNotFoundError:
        try:
            pickleStockYmd(datestr)
            dfNDaysAgo = __getStockPickle(datestr)
            if dfNDaysAgo.size == 0:
                raise Exception
        except Exception as e:
            print(e,'   -   failed to create pickle for ',datestr)
            exit(-1)
    return dfNDaysAgo


def getRowNDaysAgo(ndays):
    symbols = md.getPortfoliosSymbols()
    if (ndays == 0):
        dfDaysAgo = yf.download(tickers = symbols,period = "1d",interval = "1d",group_by = 'column',auto_adjust = True,prepost = False,threads = True)
        dfDaysAgo = dfDaysAgo.tail(1)
    elif ndays == 1:
        dfDaysAgo = yf.download(tickers=symbols, period="2d", interval="1d", group_by='column', auto_adjust=True,prepost=False, threads=True)
        dfDaysAgo = dfDaysAgo.head(1)
    else:
        start, end = getNDateAndToday(ndays)
        dfDaysAgo = yf.download(tickers = symbols,interval = "1d",start=start,end=end,group_by = 'column',auto_adjust = True,prepost = False,threads = True)
        dfDaysAgo = dfDaysAgo.head(1)
    return dfDaysAgo[['Close','Volume']]

def pickleStock(ndays):
    dfnrow = getRowNDaysAgo(ndays)
    if len(dfnrow.index.values) == 0:
        print('{} {}'.format('Failed',ndays))
        raise ConnectionError('{} {}'.format('Failed',ndays))
    rdate = getRowYmdDate(dfnrow)
    dfnrow.to_pickle(getPickleName(rdate))

def pickleStockYmd(datestr):
    ndays = getNBusDaysFromDateStr(datestr)
    pickleStock(ndays)
