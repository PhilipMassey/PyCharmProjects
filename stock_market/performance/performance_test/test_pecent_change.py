import performance as pf
import market_data as md
week=(5,1)
df_stock = pf.get_today_sym_port_perc_periods(week, incl=md.sa)
print(df_stock)

#get_symbol_port_perc_vol