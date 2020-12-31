import market_data as md

def getRow(ndays):
    #print('{:d}'.format(ndays))
    df = md.getStockPickleNBDays(ndays)
    dt = md.getRowYmdDate(df)
    print('{:d} {}'.format(ndays,dt))

[getRow(ndays) for ndays in range(0,1)]
