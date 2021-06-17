import os
import pandas as pd
import robin_stocks as r
import configparser

config = configparser.RawConfigParser()
configFilePath = '/Users/philipmassey/.tokens/robinhood.cfg'
config.read(configFilePath)
rhuser = config.get('login', 'user')
rhpwd = config.get('login', 'pwd')
login = r.login(rhuser,rhpwd)

ticker='DM'
fundamentals = r.get_fundamentals(ticker)[0]
print(fundamentals)
print(fundamentals['sector'])
print(fundamentals['industry'])