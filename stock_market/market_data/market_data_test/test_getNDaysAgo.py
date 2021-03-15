import market_data as md


def testndays(ndays):
    print('ndays ',ndays)
    start,end = md.getNDateAndToday(ndays)
    print(start,end)

def testrowndays(ndays):
    symbols = md.getAllPortfoliosSymbols()
    df = md.getRowNDaysAgo(ndays,symbols)
    print(df)


ndays=0
testndays(ndays)
testrowndays(ndays)

# [testndays(i) for i in [0,1,2,3,4,5,6,7,8]]