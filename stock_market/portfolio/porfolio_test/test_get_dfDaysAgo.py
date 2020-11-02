import portfolio as pf
import market_data as md

ndays = 0
start,end = md.getNDaysAgo(ndays)
print(start,end)
dfNDaysAgo = md.getNDaysStockPickle(ndays)
print(dfNDaysAgo)