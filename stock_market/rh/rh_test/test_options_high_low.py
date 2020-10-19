import rh
r = rh.r

symbol = 'HD'
expiration_dates = r.get_chains(symbol)['expiration_dates']
print(expiration_dates)
span = 'day'
df_expirationDates = rh.getStrikesOHLCChangesExpiration(symbol,expiration_dates,'call',span)