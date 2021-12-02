import market_data as md

ndays = 1
symbols = md.get_symbols('test')
#print('number of symbols: ',len(symbols))
df = md.get_yahoo_ndays_ago(ndays,symbols)
print(df)