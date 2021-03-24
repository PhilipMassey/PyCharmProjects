import market_data as md

symbols = md.getAllPortfoliosSymbols()

start = 0
end = 360
[md.updateMdbWithMissingRow(ndays,symbols) for ndays in range(start,end)]
