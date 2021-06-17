import market_data as md
from pprint import pprint
from datetime import datetime
from pymongo import MongoClient
client = MongoClient()
db = client[md.db_client]
db_coll_close = db[md.db_close]
db_coll_vol = db[md.db_vol]

col_name = 'NOVN'
print('total documents',db_coll_vol.count_documents({col_name:{'$gte':0}}))
#### DROP COLUMN
result = db_coll_vol.update_many( {col_name:{'$gte':0}}, { '$unset': { col_name: '' } } )

print(result.matched_count, result.modified_count)
