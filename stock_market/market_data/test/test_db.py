import market_data as md
from pymongo import MongoClient


client = MongoClient()
db = client[md.db_client]

db_coll_close = db[md.db_close]
db_coll_vol = db[md.db_vol]

ndays = 1
symbols = md.get_symbols(md.all)
symbols = ['TPCO','VREOF']
df = md.get_mdb_row(ndays,md.db_close,symbols)
#df = md.getdf_ndays_mdb_row(ndays,db_coll_close)
print('symbols size {} columns size {}'.format(len(symbols),df.columns.size))
print(df)
