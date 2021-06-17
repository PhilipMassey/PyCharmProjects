import market_data as md
from pymongo import MongoClient


client = MongoClient()
db = client[md.db_client]

db_coll_close = db[md.db_close]
db_coll_vol = db[md.db_vol]
db_5days_up = db[md.db_5days_up]
#print('total documents',db_coll_close.count_documents({'NOVN':{'$gte':0}}))

symbols = ['Date','NOVN']
#mdb_data = db_coll_close.find({'NOVN':{'$gte':0}},symbols)
#print(list(mdb_data))
#symbols = ''
ndays = 0
symbols = md.get_symbols(md.all)
#symbols.append('Date')
df = md.get_mdb_row(ndays,md.db_close,symbols)
#df = md.getdf_ndays_mdb_row(ndays,db_coll_close)
print('columns size',df.columns.size)

start = 5
days_step = (25,5)
#df = md.get_df_mdb_nrows_step(start,days_step, coll_name,symbols)
#print(df)

ndays = 5
ndays_to = 2
symbols = ['ACRS', 'AMPE', 'CTXR', 'IGXT', 'JAGX', 'NOVN']
#symbols = md.get_symbols(md.all)
symbols.append('Date')
df = md.get_df_mdb_rows(ndays, md.db_close, symbols, ndays_to)
#print(df.size)
