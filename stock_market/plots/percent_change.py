from datetime import datetime, timedelta
import calendar

import pandas as pd
import yfinance as yf
import plotly.express as px

def getNDaysAgo(ndays):
    now = datetime.now()
    start = now - pd.tseries.offsets.BusinessDay(n=(ndays+1))
    end = now - pd.tseries.offsets.BusinessDay(n=ndays)
    start = '{:%Y-%m-%d}'.format(start)
    end = '{:%Y-%m-%d}'.format(end)
    return start,end

def getPricesNDaysAgo(symbols,ndays):
    start, end = getNDaysAgo(ndays)
    #print(start,end)
    return yf.download(tickers = symbols,interval = "1d",start=start,end=end,group_by = 'column',auto_adjust = True,prepost = False,threads = True)

def getPercentVolPortfolio(dfToday,dfDaysAgo,df_port):
    dfAll = pd.concat([dfDaysAgo[['Close']],dfToday[['Close']]])
    df_pc = dfAll.Close.pct_change(periods=1)
    df_pc = df_pc.iloc[1:]
    df_stock = df_pc.reset_index(drop=True, inplace=False).T.rename(columns = {0:'percent'}, inplace = False)
    df_stock['percent'] = df_stock['percent'].apply(lambda x:round(x*100,2))
    df_stock = pd.concat([df_stock,df_port],axis=1)
    df_vol = dfToday.Volume.iloc[:1].reset_index(drop=True, inplace=False).T.rename(columns = {0:'volume'}, inplace = False)
    df_stock['volume'] = df_vol['volume']
    df_stock.reset_index(inplace=True)
    df_stock = df_stock.rename(columns = {'index':'name'})
    return df_stock

def getEndRow(symbols):
    dfEnd = yf.download(tickers = symbols,period = "1d",interval = "1d",group_by = 'column',auto_adjust = True,prepost = False,threads = True)
    dfEnd = dfEnd.tail(1)
    date = pd.to_datetime(dfEnd.index.values[0])
    date = calendar.day_name[date.weekday()]+' '+'{:%Y-%m-%d}'.format(date)
    return dfEnd,date

def getStartRow(symbols, ndays):
    dfDaysAgo = getPricesNDaysAgo(symbols,ndays)
    #dfDaysAgo.dropna(axis='columns', inplace=True)
    dfDaysAgo = dfDaysAgo.head(1)
    date = pd.to_datetime(dfDaysAgo.index.values[0])
    date = calendar.day_name[date.weekday()]+' '+'{:%Y-%m-%d}'.format(date)
    return dfDaysAgo,date

def getPortfolio():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/portfolio_symbol.csv'
    df_portfolio = pd.read_csv(path).set_index('SYMBOL')
    return df_portfolio

def plotPercentVolPortfolio(symbols, ndays,title,dfEnd,df_port):
    dfStart, start = getStartRow(symbols, ndays)
    print(start)
    print(dfStart[['Close']])
    df_stock = getPercentVolPortfolio(dfEnd, dfStart, df_port)
    df_stock.sort_values(by='percent', ascending=False, inplace=True)
    df_stock=df_stock[:40]
    df_stock.sort_values(by='PORTFOLIO',inplace=True)
    if len(title) == 0:
        title = '{} - {} percent change to {}'.format('PORTFOLIOS', start, end)
    fig = px.scatter(df_stock[:40], x="PORTFOLIO", y="percent",
                     size="volume", color="volume", title=title,
                     hover_name="name", log_x=False, log_y=False,
                     size_max=80, width=1600, height=1000)
    fig.show()

# START
df_port = getPortfolio()
symbols = list(df_port.index.values)
dfEnd, end = getEndRow(symbols)
print(end)
print(dfEnd[['Close']])

ndays = 0
plotPercentVolPortfolio(symbols,ndays,title='',dfEnd=dfEnd,df_port=df_port)
ndays = 5
title = '{} - {} days percent change'.format('PORTFOLIOS',ndays)
plotPercentVolPortfolio(symbols,ndays,title=title,dfEnd=dfEnd,df_port=df_port)
ndays = 10
title = '{} - {} days percent change'.format('PORTFOLIOS',ndays)
plotPercentVolPortfolio(symbols,ndays,title=title,dfEnd=dfEnd,df_port=df_port)
ndays = 60
title = '{} - {} days percent change'.format('PORTFOLIOS',ndays)
#plotPercentVolPortfolio(symbols,ndays,title=title,dfEnd=dfEnd,df_port=df_port)
ndays = 180
title = '{} - {} days percent change'.format('PORTFOLIOS',ndays)
#plotPercentVolPortfolio(symbols,ndays,title=title,dfEnd=dfEnd,df_port=df_port)
ndays = 365
title = '{} - {} days percent change'.format('PORTFOLIOS',ndays)
#plotPercentVolPortfolio(symbols,ndays,title=title,dfEnd=dfEnd,df_port=df_port)
