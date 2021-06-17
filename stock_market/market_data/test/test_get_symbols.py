import market_data as md


symbols = md.get_symbols(incl=md.all)
print(symbols)