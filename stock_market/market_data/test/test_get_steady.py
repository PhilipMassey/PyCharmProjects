import market_data as md
from pymongo import MongoClient

from datetime import datetime

client = MongoClient()
db = client[md.db_client]
db_5days_up = db[md.db_5days_up]

ndays = 0
adate = md.get_date_for_mdb(ndays)
print('total documents',db_5days_up.count_documents({'symbol': 'DZSI'}))
#mdb = db_5days_up.find({'symbol':'DZSI'})
#df = md.mdb_to_df(mdb)
df = md.get_df_for_symbol('DZSI',md.db_5days_up)
#df['Date'] = datetime.utcfromtimestamp(float(df['Date.$date'] / 1e3))
print(df)


#df = md.get_mdb_row_for_nday(ndays,md.db_5days_up)
#df = md.getdf_ndays_mdb_row(ndays,db_coll_close)
#print(df.symbol.values)

def get_mdb_steady(ndays,db_colln):
    df = md.get_mdb_row_for_nday(ndays, db_colln)
    return df.symbol.values

symbols = get_mdb_steady(ndays, md.db_5days_up)
print(symbols)

