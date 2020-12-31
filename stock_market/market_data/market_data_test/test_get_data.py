import market_data as md

df_port = md.getPortfolios()
print(df_port)
symbols = md.getPortfoliosSymbols()
print(symbols)
print('Fidelity {}'.format(md.getFidelitySymbols()))