# options_high_and_lows.py
"""
Functions:
    changesForExpirations returns df_expirationDates
                            ['expiration_date','begins_at', 'strike_price', 'close_price', 'high_price', 'low_price', 'open_price', 'volume']
                          calls diffMaxHighLow to print('Strike\tVolume\tHigh\tLow\tChange\tPercent')
"""
import warnings

warnings.filterwarnings("ignore")
# warnings.catch_warnings()
import robin_stocks as r
from datetime import datetime
from dateutil import tz
import pandas as pd
import plotly.express as px
from operator import itemgetter, attrgetter, methodcaller

from_zone = tz.tzutc()
to_zone = tz.tzlocal()


def utcToLocal(strDate):
    utc = datetime.strptime(strDate, '%Y-%m-%dT%H:%M:%SZ')
    utc = utc.replace(tzinfo=from_zone)
    return utc.astimezone(to_zone)


import configparser

config = configparser.RawConfigParser()
configFilePath = '/Users/philipmassey/.tokens/robinhood.cfg'
config.read(configFilePath)
rhuser = config.get('login', 'user')
rhpwd = config.get('login', 'pwd')
login = r.login(rhuser, rhpwd)


def diffMaxHighLow(df, dfstrike_prices):
    print('Strike\tVolume\tHigh\tLow\tChange\tPercent')
    for idx, row in dfstrike_prices.iterrows():
        strike_price = row.strike_price
        volume = row.volume
        df_stpr = df[(df.strike_price == strike_price)]
        high_price = max(df_stpr.high_price, default=0)
        low_price = min(df_stpr.high_price, default=0)
        diff = round((high_price - low_price), 2)
        percent = 0 if low_price == 0 else round(diff / low_price, 2)
        print(
            '${:.2f}\t{:,.0f}\t{}\t{}\t{}\t{:,.0%}'.format(strike_price, volume, high_price, low_price, diff, percent))


def changesForExpirations(symbol, expiration_dates, optionType, span, volume_limit=0):
    df_expirationDates = pd.DataFrame()
    for expirationDate in expiration_dates[0:5]:
        print('{}\t'.format(expirationDate), end='')
        options = r.find_options_for_list_of_stocks_by_expiration_date([symbol], expirationDate, optionType)
        dfoptions = pd.DataFrame((filter(lambda x: x['volume'] > volume_limit, options)))
        if dfoptions.empty:
            print('Volume is 0 for options')
        else:
            dfoptions[['strike_price', 'high_price', 'low_price']] = dfoptions[
                ['strike_price', 'high_price', 'low_price']].apply(pd.to_numeric)
            dfstrike_prices = dfoptions.sort_values(by='volume', ascending=False)[0:5][['strike_price', 'volume']]
            dfstrike_prices.sort_values(by='strike_price', inplace=True)
            # dfstrike_prices
            df_all = pd.DataFrame()
            for idx, row in dfstrike_prices.iterrows():
                strike_price = row.strike_price
                # print('Strike price: {}'.format(strike_price))
                df = pd.DataFrame(
                    r.get_option_historicals(symbol, expirationDate, strike_price, optionType, span)['data_points'])
                df['strike_price'] = strike_price
                df_all = pd.concat([df_all, df[
                    ['begins_at', 'strike_price', 'close_price', 'high_price', 'low_price', 'open_price', 'volume']]])

            df_all[['strike_price', 'high_price', 'low_price']] = df_all[
                ['strike_price', 'high_price', 'low_price']].apply(pd.to_numeric)
            df_all = df_all[df_all.high_price != 0.01]
            df_all['expiration_date'] = expirationDate
            print()
            diffMaxHighLow(df_all, dfstrike_prices)
            df_expirationDates = pd.concat([df_expirationDates, df_all])
    return df_expirationDates
