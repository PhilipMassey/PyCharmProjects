import market_data as md
from datetime import date
from datetime import datetime
import holidays
us_holidays = holidays.UnitedStates()
import os.path
from os import path
alist=[]
def checkStockPickle(ndays):
    datestr = md.getNBusDateFromNdays(ndays)
    pk_name = md.getPickleName(datestr)
    if not path.exists(pk_name):
        print('{:d},{})'.format(ndays,datestr),end=',')
        alist.append(datestr)

[checkStockPickle(ndays) for ndays in range(0,360)]
print()
print(alist)

def convertidx(idx):
    return datetime.strptime(alist[idx], '%Y-%m-%d')
a=[]
[a.append(convertidx(i)) for i in range(0,len(alist))]
for idx in range(len(a)):
    print(a[idx],a[idx] in us_holidays)