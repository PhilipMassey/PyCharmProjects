import market_data as md

symbols = md.getAllPortfoliosSymbols()

start = 6
end = 360
[md.updateMdbWithMissingRow(ndays,symbols) for ndays in range(start,end)]
