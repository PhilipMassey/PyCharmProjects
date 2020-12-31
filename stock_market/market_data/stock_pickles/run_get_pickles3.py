import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])

import market_data as md
def getRow(ndays):
    #print('{:d}'.format(ndays))
    df = md.getStockPickleNBDays(ndays)
    dt = md.getRowYmdDate(df)
    print('{:d} {}'.format(ndays,dt))

[getRow(ndays) for ndays in range(334,361)]

