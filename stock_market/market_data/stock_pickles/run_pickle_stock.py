import market_data as md
def getRow(ndays):
    #print('{:d}'.format(ndays))
    df = md.getStockPickleNBDays(ndays)
    dt = md.getRowYmdDate(df)
    print('{:d} {}'.format(ndays,dt))

[getRow(ndays) for ndays in range(1,360)]
#ndays=1
#print(md.getNBusDate(ndays))

#print(md.getNBusDaysFromDateStr('2020-04-10'))
# print(md.getNBusDaysFromDateStr('2020-02-14'))
# print(md.getNBusDaysFromDateStr('2020-02-06'))
# print(md.getNBusDaysFromDateStr('2020-02-05'))
# [getRow(ndays) for ndays in [210,211]]
