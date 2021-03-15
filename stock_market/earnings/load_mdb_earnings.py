from datetime import datetime
from pymongo import MongoClient
from bson import json_util
from pandas import json_normalize
import json
import pandas as pd
import market_data as md
import rh


client = MongoClient()
db = client['stock_market']
earnings_col = db['market_data_earnings']

symbols = md.getAllPortfoliosSymbols()
#symbols = ['HD','LOW','BEP','LU']
year,month,day = rh.getYearMonthDay()
current_month_dates = rh.getEarnings(symbols,year,month)
current_month_dates = filter(lambda x:x[1][8:10] >= day,current_month_dates)
df = pd.DataFrame(current_month_dates,columns=['symbol','earnings_date'])
df.drop_duplicates(inplace=True)

# delete current mdb records and insert new
result = earnings_col.delete_many({})
print(result.deleted_count, " documents deleted.")
try:
    result = md.addRowToMdb(df,earnings_col)
    print(len(result.inserted_ids),' documents inserted')
except Exception as e:
    print('error ',e)
