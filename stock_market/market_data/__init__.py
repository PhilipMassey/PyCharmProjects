
data_dir = '/Users/philipmassey/PycharmProjects/stock_market/market_data/data'
sa = 'seeking_alpha'
watching = 'watching'
etf = 'etf'
ark = 'ark'

all = 'ALL'
test = 'test'
db_client = 'stock_market'
db_close = 'market_data_close'
#db_close = 'test_data_close'
db_volume = 'market_data_volume'
#db_volume = 'test_data_volume'
db_5days_up = '5days_up'
db_9days_up = '9days_up'
db_5weeks_up = '5weeks_up'

db_etf_close = 'etf_close'
db_etf_vol = 'etf_vol'

from .get_csv_data import *
from .get_portfolio import *
from .stock_mdb import *
from .exchange_api import *
