import market_data as md
from datetime import datetime

def testndays(ndays):
    start,end = md.get_dates_ndays_and_today(ndays)
    print('ndays ',ndays,start,end)

def test_get_ndays_to(strdate='2020-04-01'):
    ndays = md.getNBusDaysFromDateStr(strdate)
    print('strdate ',strdate,' ndays ',ndays)
    return ndays


def test_get_period_interval(ndays=''):
    if len(ndays) == 0:
        ndays = md.get_ndays_to()
    nweeks = ndays/5
    print('ndays ',ndays,' nweeks',nweeks)
    start,end = md.get_dates_ndays_and_today(ndays)
    print(start,end)
    return ndays,nweeks




ndays=260
testndays(ndays)
md.get_period_interval(ndays=ndays)
md.get_period_interval()

#testrowndays(ndays)

# [testndays(i) for i in [0,1,2,3,4,5,6,7,8]]