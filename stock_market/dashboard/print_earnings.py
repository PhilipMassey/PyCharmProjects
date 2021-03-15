import dash
import dash_html_components as html
import dash_core_components as dcc
import market_data as md
from pymongo import MongoClient


def getCurrentMonthEarnings():
    client = MongoClient()
    db = client['stock_market']
    earnings_col = db['market_data_earnings']
    mongo_data= earnings_col.find({})
    df = md.MdbToDataframe(mongo_data)
    df.drop(['_id.$oid'], axis=1, inplace=True)
    return list(df.to_records(index=False))

alist = getCurrentMonthEarnings()
for e in alist:
    print(str(e))
