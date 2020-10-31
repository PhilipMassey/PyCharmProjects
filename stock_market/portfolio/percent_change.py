from datetime import datetime, timedelta
import calendar

import pandas as pd
import yfinance as yf

def getNDaysAgo(ndays):
    now = datetime.now()
    start = now - pd.tseries.offsets.BusinessDay(n=(ndays+1))
    end = now - pd.tseries.offsets.BusinessDay(n=ndays)
    start = '{:%Y-%m-%d}'.format(start)
    end = '{:%Y-%m-%d}'.format(end)
    return start,end

def getPricesNDaysAgo(symbols,ndays):
    start, end = getNDaysAgo(ndays)
    return yf.download(tickers = symbols,interval = "1d",start=start,end=end,group_by = 'column',auto_adjust = True,prepost = False,threads = True)

def getRowNDaysAgo(symbols, ndays):
    if ndays == 0:
        dfDaysAgo = yf.download(tickers = symbols,period = "1d",interval = "1d",group_by = 'column',auto_adjust = True,prepost = False,threads = True)
        dfDaysAgo = dfDaysAgo.tail(1)
    else:
        dfDaysAgo = getPricesNDaysAgo(symbols,ndays)
        dfDaysAgo = dfDaysAgo.head(1)
    date = pd.to_datetime(dfDaysAgo.index.values[0])
    date = calendar.day_name[date.weekday()]+' '+'{:%Y-%m-%d}'.format(date)
    return dfDaysAgo,date

def getPercentVolPortfolio(dfEnd, dfStart, df_port):
    dfAll = pd.concat([dfStart[['Close']], dfEnd[['Close']]])
    df_pc = dfAll.Close.pct_change(periods=1)
    df_pc = df_pc.iloc[1:]
    df_stock = df_pc.reset_index(drop=True, inplace=False).T.rename(columns = {0:'percent'}, inplace = False)
    df_stock['percent'] = df_stock['percent'].apply(lambda x:round(x*100,2))
    df_stock = pd.concat([df_stock,df_port],axis=1)
    df_vol = dfEnd.Volume.iloc[:1].reset_index(drop=True, inplace=False).T.rename(columns = {0: 'volume'}, inplace = False)
    df_stock['volume'] = df_vol['volume']
    df_stock.reset_index(inplace=True)
    df_stock = df_stock.rename(columns = {'index':'name'})
    return df_stock


