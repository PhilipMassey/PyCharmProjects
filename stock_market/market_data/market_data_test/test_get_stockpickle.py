import market_data as md
from datetime import datetime
ndays = 2
df = md.getStockPickleNBDays(ndays)
print(df.head(5))
#md.getStockPickle('{:%Y-%m-%d}'.format(datetime.now()))

