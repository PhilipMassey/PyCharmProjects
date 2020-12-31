import portfolio as pf
import market_data as md

ndays = 5
start,end = md.getNDatePlusOne(ndays)
print('Start {} and end {}'.format(start,end))

dfNDaysAgo = md.getStockPickle(end)
print(dfNDaysAgo)

dfNDaysAgo = md.getStockPickle(start)
print(dfNDaysAgo)
