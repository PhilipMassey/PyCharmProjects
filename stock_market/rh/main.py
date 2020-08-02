import robin_stocks as r
from datetime import datetime
from dateutil import tz


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

r = r