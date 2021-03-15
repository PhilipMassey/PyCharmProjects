import portfolio as pf
import plots as pl

ndays = 0
df_stock,endDt = pf.getSymbolPortPercentVolToday(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt,True)

ndays = 5
df_stock,endDt = pf.getSymbolPortPercentVolToday(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt,True)

ndays = 10
df_stock,endDt = pf.getSymbolPortPercentVolToday(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt,True)

ndays = 30
df_stock,endDt = pf.getSymbolPortPercentVolToday(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt,True)
