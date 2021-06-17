import market_data as md

ndays = 0
symbols = md.get_symbols(md.all)
#print('number of symbols: ',len(symbols))
md.get_yahoo_ndays_ago(ndays,symbols)