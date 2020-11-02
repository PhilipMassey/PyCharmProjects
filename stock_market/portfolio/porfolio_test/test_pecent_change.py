import portfolio as pf
import plots as pl

df_port = pf.getPortfolios()
symbols = list(df_port.index.values)
dfEnd, endDt = pf.getOneDayRow(symbols)
#print(end)
#print(dfEnd[['Close']])

ndays = 0
pl.plotPercentVolPortfolio(symbols,ndays,title='',dfEnd=dfEnd,,endDt=endDt,df_port=df_port)
ndays = 5
title = '{} - {} days percent change'.format('PORTFOLIOS',ndays)
pl.plotPercentVolPortfolio(symbols,ndays,title=title,dfEnd=dfEnd,, endDt=endDt,df_port=df_port)