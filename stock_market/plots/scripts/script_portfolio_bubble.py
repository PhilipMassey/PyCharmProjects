import portfolio as pf
import plots as pl

ndays = 1
df_stock,endDt = pf.getSymbolPortPercentVolToday(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt,False)

ndays = 5
df_stock,endDt = pf.getSymbolPortPercentVolToday(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt,False)

ndays = 10
df_stock,endDt = pf.getSymbolPortPercentVolToday(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt,False)

ndays = 30
df_stock,endDt = pf.getSymbolPortPercentVolToday(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt,False)
