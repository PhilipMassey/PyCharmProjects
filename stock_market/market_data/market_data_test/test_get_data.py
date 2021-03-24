import market_data as md

df_port = md.getPortfoliosAndSymbols()
#print(df_port)
symbols = md.getAllPortfoliosSymbols()
#print(symbols)
#print('Fidelity {}'.format(md.getFidelitySymbols()))

df = md.getdfPortfolioSymbol('sa_ratings')
print(df)