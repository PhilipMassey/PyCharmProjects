import market_data as md

ndays = 3
start, end = md.getNDateAndToday(ndays)
print(start,end)
dfCloseStart,dfVolStart = md.getMdbRowCloseVol(start)
dfCloseEnd,dfVolEnd = getMdbRowCloseVol(end)
print(strdfidxDate(dfCloseStart))
print(strdfidxDate(dfCloseEnd))