import sys

sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])

import market_data as md
import pandas as pd
from datetime import datetime

from pymongo import MongoClient
from bson import json_util, ObjectId
from pandas import json_normalize
import json

client = MongoClient()
db = client['stock_market']


def removeBadData(df):
    if 'BRK.B' in list(df.columns):
        print(df['BRK.B'])
        return df.drop(columns=['BRK.B'])
    return df


def addPicklesToMdbConn(ndays):
    print(ndays)
    dfall = md.getStockPickleNBDays(ndays, skip=True)
    if dfall.size > 0:
        df = dfall['Close']
        df = removeBadData(df)
        df.reset_index(inplace=True)
        data_dict = df.to_dict("records")
        db["market_data_close"].insert_many(data_dict)
        df = dfall['Volume']
        df = removeBadData(df)
        df.reset_index(inplace=True)
        data_dict = df.to_dict("records")
        db["market_data_volume"].insert_many(data_dict)


