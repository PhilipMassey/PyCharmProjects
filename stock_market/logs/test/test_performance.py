import market_data as md
from pymongo import MongoClient


client = MongoClient()
db = client['stock_market']
collection = db[md.db_close]
ndays = 5
adate = md.get_date_for_mdb(ndays)
query = collection.find({'Date': adate})
print( query.explain())
