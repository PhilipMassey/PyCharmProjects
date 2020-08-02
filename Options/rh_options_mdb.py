import site
site.addsitedir('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages')
import os
import sys
from datetime import datetime
import pandas as pd
import pymongo
from pymongo import MongoClient
import robin_stocks as r

import configparser
config = configparser.RawConfigParser()
configFilePath = '/Users/philipmassey/.tokens/robinhood.cfg'
config.read(configFilePath)
rhuser = config.get('login', 'user')
rhpwd = config.get('login', 'pwd')
login = r.login(rhuser,rhpwd)


client = MongoClient()
db = client['robinhood_options']

ticker = sys.argv[1]
if ticker is None:
    print('ticker not entered on commandline')
    exit(code=404)
today = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
print('{0}\t{1}'.format(ticker,today))
chains = r.get_chains(ticker)
expiration_dates = chains['expiration_dates']
for expiration_date in expiration_dates:
    try:
        stock_options = r.find_options_for_stock_by_expiration(ticker, expiration_date)
        df = pd.DataFrame(stock_options)
        quotes = r.get_quotes(ticker)
        df['ticker_last_trade_price'] = quotes[0]['last_trade_price']
        df['ticker_updated_at'] = quotes[0]['updated_at']
        df['_id'] = df['expiration_date'] + '_' + df['strike_price'] + '_' + df['ticker_updated_at'] + '_' + df['type']

        data_dict = df.to_dict(orient='records')

        try:
            db[ticker].insert_many(data_dict)
        except pymongo.errors.DuplicateKeyError as e:
            print(e.error_document)
        except Exception as ee:
            print(ee)
    except Exceptions as ee:
        print(ee)
print('{0}\t{1}'.format(ticker,'Completed'))
