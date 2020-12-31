import portfolio as pf

ndays = 1
df_stock,endDt = pf.getSymbolPortPercentVol(ndays)
print(endDt)
print(df_stock)