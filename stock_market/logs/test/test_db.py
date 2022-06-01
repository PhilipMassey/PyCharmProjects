import sys; sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])
import market_data as md
from pymongo import MongoClient
from bson import json_util
from pandas import json_normalize
import json
import pandas as pd
client = MongoClient()
db = client['stock_market']

symbols = ['TLT','EDV','Date']
ndays = 1
adate = md.get_date_for_mdb(ndays)
print(adate)

count = md.mdb_document_count(ndays, md.db_close)
print('count',count)

db_coll = db[md.db_close]
mdb_data = db_coll.find({'Date': adate})
for c in mdb_data:
    print(c)
mdb_data = db_coll.find({'Date': adate}, symbols)
for c in mdb_data:
    print(c)
df = md.mdb_to_df(mdb_data)
#print('size',df.size)


df = md.get_df_from_mdb_for_nday(ndays, md.db_close, symbols)
print('size',df)



df = md.get_df_from_mdb_for_nday(ndays,md.db_close)
#print('df',df)