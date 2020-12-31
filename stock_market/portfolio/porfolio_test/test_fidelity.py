import portfolio as pf
ndays = 1
df_stock,endDay = pf.getFidelityStockPercentVolPort(ndays)
print(df_stock)