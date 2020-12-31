import market_data as md

def testbackforth(ndays):
    datestr = md.getNBusDateFromNdays(ndays)
    ndays = md.getNBusDaysFromDateStr(datestr)
    print('{} - {} - {}'.format(ndays,datestr,ndays))

[testbackforth(ndays) for ndays in range(0,10)]