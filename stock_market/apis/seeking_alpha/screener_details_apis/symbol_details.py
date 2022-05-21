import pandas as pd
import market_data as md
from pymongo import MongoClient
client = MongoClient()
db = client['stock_market']
db_coll_name = 'symbol_detail'


def display_index():
    df = md.get_df_from_mdb_columns([],db_coll_name)
    print(set(df.index))

def add_to_mdf(df,db_coll_name):
    results = md.add_df_to_db(df, db_coll_name, dropidx=False)
    print(len(results.inserted_ids))