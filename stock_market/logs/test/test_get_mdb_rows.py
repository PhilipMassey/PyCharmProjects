import market_data as md
from pymongo import MongoClient


client = MongoClient()
db = client[md.db_client]

db_coll_close = db[md.db_close]
db_coll_vol = db[md.db_volume]

start = 0
end = 5
ndays = 6
symbols = ['TLT','MDB']
mdb_data = md.get_df_from_mdb_for_nday(ndays, md.db_close, symbols = symbols)
# adate = md.get_dates_ndays_and_today(ndays)
# db_coll = db[md.db_close]
# mdb_data = db_coll_close.find({db_coll: adate})
df = md.mdb_to_df(mdb_data, dateidx=False)
print(df)