import yfinance as yf
import market_data as md

def get_yahoo_ndays_ago(ndays, symbols):
    print('{} days ago {} symbols.'.format(ndays,len(symbols)))
    if (ndays == 0):
        dfDaysAgo = yf.download(tickers = symbols,period = "1d",interval = "1d",group_by = 'column',auto_adjust = True,prepost = False,threads = True)
        dfDaysAgo = dfDaysAgo.tail(1)
    elif ndays == 1:
        dfDaysAgo = yf.download(tickers=symbols, period="2d", interval="1d", group_by='column', auto_adjust=True,prepost=False, threads=True)
        dfDaysAgo = dfDaysAgo.head(1)
    else:
        start, end = md.get_dates_ndays_and_today(ndays)
        dfDaysAgo = yf.download(tickers = symbols,interval = "1d",start=start,end=end,group_by = 'column',auto_adjust = True,prepost = False,threads = True)
        dfDaysAgo = dfDaysAgo.head(1)
    return dfDaysAgo[['Close','Volume']]
