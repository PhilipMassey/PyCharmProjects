data_dir = '/Users/philipmassey/PycharmProjects/stock_market/market_data/data'

#FOLDERS
all = 'ALL'
ark = 'ARK'
etf = 'ETF'
holding = 'Holding'
sa = 'Seeking_Alpha'
test = 'test'
watching = 'Watching'
db_client = 'stock_market'
db_close = 'market_data_close'
db_volume = 'market_data_volume'
db_test_close = 'test_close'
db_test_vol = 'test_volume'
db_symbol_profile = 'symbol_profile'


from .csv_data_defs import *
from .portfolio_defs import *
from .stock_mdb import *
from .exchange_api import *


test_symbols = 'test_symbols'
top_growth_stocks = 'Top Growth Stocks'
top_reits = 'Top REITs'
top_rated_dividend_stocks = 'Top Rated Dividend Stocks'
top_rated_stocks = 'Top Rated Stocks'
top_small_cap_stocks = 'Top Small Cap Stocks'
top_stocks_by_quant = 'Top Stocks by Quant'
top_stocks_in_renewable_electricity = 'Top Stocks in Renewable Electricity'
top_value_stocks = 'Top Value Stocks'
utilities = 'Utilities'
utilities_renewable_energy = 'Utilities-Renewable Energy'
water_etf = 'Water ETF'

sa_ports = ['Top Communication Stocks', 'Top Consumer Discretionary Stocks', 'Top Consumer Staples Stocks',
            'Top Financial Stocks', 'Top Growth Stocks', 'Top Healthcare Stocks', 'Top Industrial Stocks',
            'Top Materials Stocks', 'Top Quant Dividend Stocks', 'Top Rated Dividend Stocks', 'Top Rated Stocks',
            'Top Real Estate Stocks', 'Top REITs', 'Top Small Cap Stocks', 'Top Stocks by Quant',
            'Top Stocks Under $10', 'Top Technology Stocks', 'Top Utility Stocks', 'Top Value Stocks',
            'Top Yield Monsters']
sc_port = 'Stock Card Value and Momentum'