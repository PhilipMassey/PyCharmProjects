from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

def getStartEndDates(period):
    now = datetime.now()
    end = '{:%Y-%m-%d}'.format(now)
    start = now - pd.tseries.offsets.BusinessDay(n = period)
    start = '{:%Y-%m-%d}'.format(start)
    return start,end

def getPricesForDay(names,day):
    tickers = yf.Tickers(names)
    start, end = getStartEndDates(period=1)
    return tickers.history(interval='1d', start=start, end=end)


names = ['AAPL','MSFT','SHOP','SQ']
tickers = yf.Tickers(names)
start,end = getStartEndDates(period=1)
df = tickers.history(interval='1d',start=start,end=end)
df_pc = df.Close.pct_change(periods=1).dropna()#,freq=pd.offsets.BDay())
df_stock = df_pc.reset_index(drop=True, inplace=False).T.rename(columns = {0:'percent'}, inplace = False)
df_stock['percent'] = df_stock['percent'].apply(lambda x:round(x*100,2))
#df_stock

start,end = getStartEndDates(period=2)
print(start,end)
df = tickers.history(interval='1d',start=start,end=end)
df
