import pandas as pd
import yfinance as yf
import market_data as md

def get_yahoo_ndays_ago(ndays, symbols):
    if 'Date' in symbols:
        symbols.remove('Date')
    if len(symbols) == 0:
        df = pd.DataFrame({})
    elif ndays == 0:
        df = yf.download(tickers=symbols, period="1d", interval="1d", group_by='column', auto_adjust=True,
                         prepost=True, threads=True)
    elif ndays == 1:
        df = yf.download(tickers=symbols, period="2d", interval="1d", group_by='column', auto_adjust=False,
                         prepost=False, threads=True)
    else:
        start, end = md.get_dates_ndays_and_today(ndays)
        df = yf.download(tickers=symbols, interval="1d", start=start, end=end, group_by='column',
                         auto_adjust=True, prepost=True, threads=True)
        #df.drop('FB', axis=1, level=1, inplace=True, errors='ignore')
        df = df.dropna(axis=1, how='all')
    strdate = md.get_mdb_strdate_for_ndays(ndays)
    if strdate in df.index:
        df = df.loc[[strdate]]
    else:
        df = pd.DataFrame({})
    #df.drop('FB', axis=1, level=1, inplace=True, errors='ignore')
    df = df.dropna(axis=1, how='all')
    if df.size == 0:
        return pd.DataFrame({})
    else:
        return df[['Close', 'Volume']]
