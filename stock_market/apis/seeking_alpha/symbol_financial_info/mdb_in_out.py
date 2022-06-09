import market_data as md
import pandas as pd

from bson import json_util
from pandas import json_normalize
import json
from pymongo import MongoClient
client = MongoClient()
db = client[md.db_client]



def df_symbol_profile(symbols=[],fields=None) -> list:
    coll_name = md.db_symbol_profile
    db_coll = db[coll_name]
    if len(symbols) == 0:
        mongo_data = db_coll.find()
    else:
        mongo_data = db_coll.find({"symbol": {"$in": symbols}},fields)
    sanitized = json.loads(json_util.dumps(mongo_data))
    df = json_normalize(sanitized)
    df.drop(columns=['_id.$oid'],inplace=True)
    return df


def dct_mdb_symbol_fields(symbols=[],fields=None) -> dict:
    df = df_symbol_profile(symbols, fields)
    df.set_index('symbol',inplace=True)
    return pd.DataFrame.to_dict(df)


def dct_mdb_symbol_names(symbols=[]) -> dict:
    fields = ['symbol','companyName']
    dct = dct_mdb_symbol_fields(symbols,fields)
    return dct["companyName"]


def dct_mdb_symbol_industry_sector(symbols=[]) -> dict:
    fields = ['symbol','sectorname','primaryname']
    dct = dct_mdb_symbol_fields(symbols,fields)
    return dct['sectorname'],dct['primaryname']



# def dct_mdb_symbol_names(symbols=[]) -> dict:
#     coll_name = md.db_symbol_profile
#     db_coll = db[coll_name]
#     if len(symbols) == 0:
#         mongo_data = db_coll.find()
#     else:
#         mongo_data = db_coll.find({"symbol" : { "$in" : symbols}})
#     sanitized = json.loads(json_util.dumps(mongo_data))
#     df = json_normalize(sanitized)
#     dct_sn = {}
#     for idx in range(df.shape[0]):
#         dct_sn[df.iloc[idx].symbol] = df.iloc[idx]['profile.companyName']
#     return dct_sn


