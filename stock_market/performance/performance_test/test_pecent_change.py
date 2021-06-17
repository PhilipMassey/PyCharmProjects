import performance as pf
import market_data as md
week=(5,1)
df_stock = pf.getTodaySymPortPercPeriods(week,incl=md.sa)
print(df_stock)

#getSymbolPortPercentVol