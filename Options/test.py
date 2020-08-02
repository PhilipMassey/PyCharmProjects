import os
import site
site.addsitedir('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages')

from datetime import datetime
import pandas as pd
import pymongo
from pymongo import MongoClient
import robin_stocks as r
import sys

import os
import robin_stocks as r
import configparser
config = configparser.RawConfigParser()
configFilePath = '/Users/philipmassey/.tokens/robinhood.cfg'
config.read(configFilePath)
print(list(config.items()))
rhuser = config.get('login', 'user')
rhpwd = config.get('login', 'pwd')
print(rhuser,rhpwd)
login = r.login(rhuser,rhpwd)


client = MongoClient()
db = client['robinhood_options']
symbol='NET'
print(r.get_quotes(symbol)[0]['last_trade_price'])
print(r.get_quotes(symbol)[0]['updated_at'])
symbol = 'HD'
expiration_dates = r.get_chains(symbol)['expiration_dates']
print(expiration_dates)
expirationDate = expiration_dates[0]
volume_limit = 0
print('running')
optionData = r.find_options_for_list_of_stocks_by_expiration_date([symbol], expirationDate=expirationDate,optionType='call')
dfoptions = pd.DataFrame((filter(lambda x:x['volume']>volume_limit,optionData)))
dfstrikes = dfoptions[['strike_price','volume']].sort_values(by='volume', ascending=False)
strike_prices = [i for i in enumerate(dfstrikes[0:5].strike_price)]
print(strike_prices)
