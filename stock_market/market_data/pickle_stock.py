import portfolio as pf
import pandas as pd
import yfinance as yf
import calendar
from datetime import datetime

def getStockPickleDirectory():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/stock_pickles'
    return path
def getPickleName(rdate):
    ppath = getStockPickleDirectory()
    return ppath+'/'+rdate+'.pk'

def getNDaysAgo(ndays):
    now = datetime.now()
    start = now - pd.tseries.offsets.BusinessDay(n=(ndays+1))
    end = now - pd.tseries.offsets.BusinessDay(n=ndays)
    start = '{:%Y-%m-%d}'.format(start)
    end = '{:%Y-%m-%d}'.format(end)
    return start,end

def getDescriptiveDate(dfRow):
    date = pd.to_datetime(dfRow.index.values[0])
    return calendar.day_name[date.weekday()]+' '+'{:%Y-%m-%d}'.format(date)

def getRowYmdDate(dfRow):
    rowdate =  pd.to_datetime(dfRow.index.values[0])
    return '{:%Y-%m-%d}'.format(rowdate)

def getNDaysStockPickle(ndays):
    start,end = getNDaysAgo(ndays)
    pk_name = getPickleName(start)
    dfNDaysAgo = pd.DataFrame()
    try:
        dfNDaysAgo = pd.read_pickle(pk_name)
    except FileNotFoundError as e:
        print(e,ndays,start)
    return dfNDaysAgo


def getRowNDaysAgo(symbols, ndays):
    if ndays == 0:
        dfDaysAgo = yf.download(tickers = symbols,period = "1d",interval = "1d",group_by = 'column',auto_adjust = True,prepost = False,threads = True)
        dfDaysAgo = dfDaysAgo.tail(1)
    else:
        start, end = getNDaysAgo(ndays)
        dfDaysAgo = yf.download(tickers = symbols,interval = "1d",start=start,end=end,group_by = 'column',auto_adjust = True,prepost = False,threads = True)
        dfDaysAgo = dfDaysAgo.head(1)
    return dfDaysAgo[['Close','Volume']]

def pickleStock(ndays):
    print(ndays)
    dfnrow = getRowNDaysAgo(symbols, ndays)
    if len(dfnrow.index.values) == 0:
        print('{} {}'.format('Failed',ndays))
        exit()
    rdate = getRowYmdDate(dfnrow)
    dfnrow.to_pickle(getPickleName(rdate))
