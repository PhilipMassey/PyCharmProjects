
data_dir = '/Users/philipmassey/PycharmProjects/stock_market/market_data/data'
sa = 'seeking_alpha'
watching = 'watching'
all = 'ALL'
db_client = 'stock_market'
db_close = 'market_data_close'
db_vol = 'market_data_volume'
db_5days_up = '5days_up'
db_9days_up = '9days_up'
db_5weeks_up = '5weeks_up'
csv_filesy = ['Alternative Medicine',
             'Comm Services','Comm Services - Comm Equip',
             'Consumer Disc','Consumer Disc-Auto Manu Value','Consumer Disc-Auto Manu Profit','Consumer Disc-Internet & Direct','Consumer Disc-Home building','Consumer Disc-Home Furnish & Retail',
             'Consumer Staples',
             'Financials',
             'Health Care','Health Care-Biotech','Health Care-Pharmaceuticals','Health Care-Pharmaceuticals Momentum',
             'Industrials','Industrials-Value','Industrials-Growth','Industrials-Profitability','Industrials-EPS',
             'Industrials-Construction Materials','Industrials-Electrical Comp & Equip','Industrials-Infrastructure','Industrials-Marine','Industrials-Trucking',
             'Inf Tech','Inf Tech-Value','Inf Tech-Growth','Inf Tech-Profitability','Inf Tech-EPS',
             'Inf Tech-Application Software','Inf Tech-Semicond Equip','Inf Tech-Semiconductors','Inf Tech-Internet Serv & Infr',
             'Inf Tech-Tech Hardware','Inf Tech-Systems Software','Inf Tech-Data Proc & Out',
             'Materials','Materials-Growth','Materials-Steel','Materials-Lumber',
             'Top Growth', 'Top Rated', 'Top REITs','Top Small','Top Tech','Top Value',
             'Utilities','Utilities-Renewable Energy'
             ]
from .get_csv_data import *
from .get_portfolio import *
from .stock_mdb import *
from .exchange_api import *
