import portfolio as pf
import plots as pl

df_port = pf.getPortfolios()
print(df_port.head())
symbols = list(df_port.index.values)
dfEnd, endDt = pf.getOneDayRow(symbols)
print(dfEnd[['Close']])
