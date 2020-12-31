import market_data as md
import portfolio as pf
import pandas as pd
pd.set_option('display.max_rows', 500)
ndays = 0
start,end = md.getNDatePlusOne(ndays)
dfEnd = md.getStockPickle(end)
endDt = md.getDescriptiveDate(dfEnd)
dfStart = md.getStockPickle(start)
startDt = md.getDescriptiveDate(dfStart)
print(startDt,endDt)
df_stock = pf.getStockPercentVol(dfEnd, dfStart)
print(df_stock)
