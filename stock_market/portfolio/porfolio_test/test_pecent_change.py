import portfolio as pf

ndays = 1
df_stock,endDt = pf.getSymbolPortPercentVolToday(ndays)
print(endDt)
print(df_stock)