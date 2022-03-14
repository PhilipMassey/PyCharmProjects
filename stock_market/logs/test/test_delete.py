import market_data as md
from pprint import pprint
from datetime import datetime
from pymongo import MongoClient
client = MongoClient()
db = client['test_database']

collection = db['test_collection']
rec = {"author":"Dave","text":"My first blog post!","tags":["mongodb","python","pymongo"],"date":{"date":"2019-11-24T21:30:30.702Z"}}
#id = collection.insert_one(rec)
print('inserted: ',id)
print('count documents: ',collection.count_documents({'author':'Dave'}))
#cursor = collection.find({'author':'Dave'})
#for document in cursor:
#    pprint(document)

#result = collection.delete_one({"author": "Dave"})
#result = collection.delete_many({"author": "Dave"})
#print('deleted: ',result.deleted_count)
#print('count documents: ',collection.count_documents({'author':'Dave'}))


{"_id":{"$oid":"5ddaf676b71a3f348a15bebc"},"author":"Mike","text":"My first blog post!","tags":["mongodb","python","pymongo"],"date":{"$date":"2019-11-24T21:30:30.702Z"}}

### ADD COLUMN
col_name = 'cost'
result = collection.update_many({"author": 'Dave'}, {"$set": {col_name: 3.3}})
print(result.matched_count, result.modified_count)

#### DROP COLUMN
col_name = 'cost'
result = collection.update_many( { }, { '$unset': { col_name: '' } } )
print(result.matched_count, result.modified_count)
