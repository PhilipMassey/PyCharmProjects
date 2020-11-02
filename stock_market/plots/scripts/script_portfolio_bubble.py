import portfolio as pf
import plots as pl
ndays = 1
df_stock,endDt = pf.getPercentVolPort(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt)

ndays = 5
df_stock,endDt = pf.getPercentVolPort(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt)

ndays = 10
df_stock,endDt = pf.getPercentVolPort(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt)

ndays = 30
df_stock,endDt = pf.getPercentVolPort(ndays)
pl.plotPercentVolPortfolio(df_stock,ndays,endDt)
