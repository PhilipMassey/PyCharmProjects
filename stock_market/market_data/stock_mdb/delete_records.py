import market_data as md
from datetime import datetime
import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client['stock_market']

# delete all
#results = db[db_coll_name].remove({})
#results.values()



def delete_row_for_day(ndays):
    adate = md.get_date_for_mdb(ndays)
    db_coll = db[md.db_close]
    db_coll.delete_one({'Date': adate})
    db_coll = db[md.db_volume]
    db_coll.delete_one({'Date': adate})

def count_and_delete_for_day(ndays):
    db_coll_name = md.db_close
    db_coll = db[db_coll_name]
    df = md.get_df_from_mdb(ndays, db_coll_name)
    print(df)
    adate = md.get_date_for_mdb(ndays)
    adate
    db_coll.delete_many({'Date': adate})
    df = md.get_df_from_mdb(ndays, db_coll_name)
    print(df)