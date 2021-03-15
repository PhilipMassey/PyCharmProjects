import market_data as md
import pandas as pd


def getStockPickleDirectory():
    path = '/market_data/stock_pickles'
    return path

def getPickleName(yymmdd):
    ppath = getStockPickleDirectory()
    return ppath+'/'+yymmdd+'.pk'


def getStockPickleDirectory():
    path = '/market_data/stock_pickles'
    return path

def getPickleName(rdate):
    ppath = getStockPickleDirectory()
    return ppath+'/'+rdate+'.pk'

def __getStockPickle(datestr):
    pk_name = getPickleName(datestr)
    return pd.read_pickle(pk_name)

# def getStockPickleNBDays(ndays):
#     datestr = md.getNBusDateFromNdays(ndays)
#     return getStockPickle(datestr)

def getStockPickleNBDays(ndays,skip=False):
    datestr = getNBusDateFromNdays(ndays,skip)
    if datestr == 'SKIP':
        return pd.DataFrame({})
    else:
        return md.getStockPickle(datestr)

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


def pickleStock(ndays):
    symbols = md.getAllPortfoliosSymbols()
    dfnrow = getRowNDaysAgo(ndays,symbols)
    if len(dfnrow.index.values) == 0:
        print('{} {}'.format('Failed',ndays))
        raise ConnectionError('{} {}'.format('Failed',ndays))
    rdate = getRowYmdDate(dfnrow)
    dfnrow.to_pickle(getPickleName(rdate))

def pickleStockYmd(datestr):
    ndays = getNBusDaysFromDateStr(datestr)
    pickleStock(ndays)
