import market_data as md
from pprint import pprint
from datetime import datetime
from pymongo import MongoClient
client = MongoClient()
db = client[md.db_client]
db_coll = db[md.db_close]
#db_coll = db[md.db_volume]

#### DROP COLUMN

col_name = 'FB'
print('total documents',db_coll.count_documents({col_name:{'$gte':0}}))
result = db_coll.update_many( {col_name:{'$gte':0}}, { '$unset': { col_name: '' } } )

print(result.matched_count, result.modified_count)
