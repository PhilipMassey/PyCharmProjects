import yfinance as yf
import market_data as md

def get_yahoo_ndays_ago(ndays, symbols):
    if 'Date' in symbols:
        symbols.remove('Date')
    if len(symbols) == 1:
        if type(symbols) == list:
            symbols.append('FB')
        else:
            symbols.add('FB')
        print(symbols,'{} days ago {} symbols from yahoo.'.format(ndays,len(symbols)-1))
    if (ndays == 0):
        df = yf.download(tickers = symbols, period ="1d", interval ="1d", group_by ='column', auto_adjust = True, prepost = False, threads = True)
        df = df.tail(1)
    elif ndays == 1:
        df = yf.download(tickers=symbols, period="2d", interval="1d", group_by='column', auto_adjust=True, prepost=False, threads=True)
        df = df.head(1)
    else:
        start, end = md.get_dates_ndays_and_today(ndays)
        df = yf.download(tickers = symbols, interval ="1d", start=start, end=end, group_by ='column', auto_adjust = True, prepost = False, threads = True)
        df = df.head(1)
        df.drop('FB', axis=1, level=1, inplace=True, errors='ignore')
        df = df.dropna(axis=1, how='all')
    return df[['Close', 'Volume']]
