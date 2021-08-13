import market_data as md
from pymongo import MongoClient

import rh
r = rh.r

def getEarningsFromRH():
    symbols = md.get_symbols(incl=md.all)
    year,month,day = rh.getYearMonthDay()
    current_month_dates = rh.getEarnings(symbols,year,month)
    current_month_dates = filter(lambda x:x[1][8:10] >= day,current_month_dates)
    return current_month_dates
def getCurrentMonthEarningsMdb():
    client = MongoClient()
    db = client['stock_market']
    earnings_col = db['market_data_earnings']
    mongo_data = earnings_col.find({})
    df = md.mdb_to_df(mongo_data)
    df.drop(['_id.$oid'], axis=1, inplace=True)
    return list(df.to_records(index=False))

earnings = getCurrentMonthEarningsMdb()
for e in earnings:
    print(e[0], '\t', e[1])
