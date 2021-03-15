import market_data as md

symbols = md.getAllPortfoliosSymbols()

start = 120
end = 360
[md.addPicklesToMdbConn(ndays) for ndays in range(start,end)]

[md.updateMdbWithMissingRow(ndays,symbols) for ndays in range(start,end)]
