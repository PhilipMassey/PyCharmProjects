import market_data as md


#port_sym = md.get_port_and_symbols(incl=md.all)
#print(len(port_sym),'  ', port_sym)

symbol = md.get_symbols(incl=md.all)
print(len(symbol),'  ', symbol)
