import rh
r = rh.r
symbol = 'UFPI'
expiration_dates = r.get_chains(symbol)['expiration_dates']
print(expiration_dates)

# Earnings
#import pandas as pd
#df_options = pd.DataFrame(r.options.get_open_option_positions())
#positions = df_options['chain_symbol']
#positions = ['CXW']
#rh.getEarnings(positions)

# RH Options high low changes
span = 'day'
df_expirationDates = rh.getStrikesOHLCChangesExpiration(symbol, expiration_dates, 'call', span)
print(df_expirationDates)

# RH Plot Multiple Strikes
expirationDate = expiration_dates[0]
dfstrike_prices = rh. getStrikePrices(symbol,expirationDate)
print(dfstrike_prices)
span = 'day'
span = 'week'
ohlc = 'close_price'
rh.plotPricesForExpriation(ohlc,symbol,expirationDate,dfstrike_prices,span=span)