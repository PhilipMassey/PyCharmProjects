import market_data as md

import pandas as pd
import rh
r = rh.r

df_options = pd.DataFrame(r.options.get_open_option_positions())
if len(df_options) == 0:
    print('No Options')
else:
    positions = df_options['chain_symbol']
    #positions = ['MOMO']
    rh.getEarnings(positions)


symbols = md.getPortfoliosSymbols()
current_year_dates = rh.getEarnings(symbols)
for e in current_year_dates:
    print(e[0], '\t', e[1])