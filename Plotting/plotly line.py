
from datetime import datetime
from dateutil import tz

from_zone = tz.tzutc()
to_zone = tz.tzlocal()
def utcToLocal(strDate):
    utc = datetime.strptime(strDate, '%Y-%m-%dT%H:%M:%SZ')
    utc = utc.replace(tzinfo=from_zone)
    return utc.astimezone(to_zone)

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')


import robin_stocks as r
from datetime import datetime
from dateutil import tz
import pandas as pd
import plotly.express as px

import configparser
config = configparser.RawConfigParser()
configFilePath = '/Users/philipmassey/.tokens/robinhood.cfg'
config.read(configFilePath)
rhuser = config.get('login', 'user')
rhpwd = config.get('login', 'pwd')
login = r.login(rhuser,rhpwd)

symbol = 'SPG'
df = pd.DataFrame(r.get_historicals(symbol,span='week',bounds='regular')) # 'day', 'week', 'year', or '5year'. Default is 'week'.
local = utcToLocal(df.iloc[-1:].begins_at.values[-1])
title = '{} {}'.format(symbol, local)


#fig = px.line(df, x='begins_at', y='close_price')

fig = px.scatter(df, x='begins_at', y='close_price',
                 title="Hide Gaps with rangebreaks")
# fig.update_xaxes(
#     range=[
#         dict(bounds=["May 17", "May 18"])
#     ]
# )
fig.show()