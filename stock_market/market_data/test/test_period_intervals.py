import market_data as md

from datetime import datetime
date_format = "%Y-%m-%d"
alist = []
for ndays in md.get_ndays_range_wfm3612():
    dtstr = md.get_busdate_ndays_ago(ndays)
    dt = datetime.strptime(dtstr, date_format)
    alist.append(dt)
    print(dtstr,end=', ')
print()
for idx in range(1,len(alist)):
    print((alist[0] - alist[idx]).days,end=', ')
print()
alist = []
for ndays in md.get_ndays_range_montlhly():
    dtstr = md.get_busdate_ndays_ago(ndays)
    dt = datetime.strptime(dtstr, date_format)
    alist.append(dt)
    print(dtstr,end=', ')
print()
for idx in range(1,len(alist)):
    print((alist[idx-1] - alist[idx]).days,end=', ')
