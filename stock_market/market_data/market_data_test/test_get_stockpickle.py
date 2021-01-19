import market_data as md
from datetime import datetime
ndays = 7
df = md.getStockPickleNBDays(ndays,skip=True)
print(df.head(1))
#md.getStockPickle('{:%Y-%m-%d}'.format(datetime.now()))

