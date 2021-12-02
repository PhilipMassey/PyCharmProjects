import performance as pf
import market_data as md
import pandas as pd

print(md.get_perc_change_ndays())

ndays_range = md.get_perc_change_ndays()
df = pf.df_percents_for_range(ndays_range, ports=[md.sector_xl_etf])
print(df)

print(df.isnull().sum())
print(df.isnull().values.any())
print(df[df.notnull()])