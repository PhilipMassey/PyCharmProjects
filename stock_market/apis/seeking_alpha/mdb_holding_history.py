import pandas as pd
import market_data as md
from pymongo import MongoClient
client = MongoClient()
db = client['stock_market']
db_coll_name = 'holding history'

if __name__ == '__main__':
    df = md.get_df_from_mdb_columns([],db_coll_name)
    print('history: ',set(df.index))

    df = md.get_dir_port_symbols('Holding')
    print('current symbols; ', df.shape[0])

    strdt = md.get_mdb_strdate_for_ndays(0)
    dt = md.get_mdbdate_from_strdate(strdt)
    df['Date'] = dt
    df.set_index('Date',inplace=True)

    results = md.add_df_to_db(df, db_coll_name, dropidx=False)
    print('added current holding: ' ,len(results.inserted_ids))

    df = md.get_df_from_mdb_columns([],db_coll_name)
    print('history: ',set(df.index))

