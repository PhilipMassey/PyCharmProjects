from datetime import datetime
import pandas as pd
import rh
r = rh.r


df_options = pd.DataFrame(r.options.get_open_option_positions())
if len(df_options) == 0:
    print('No Options')
else:
    positions = df_options['chain_symbol']
    year,month,day = rh.getYearMonthDay()
    earnings = rh.getEarnings(positions,year,month)
    for e in earnings:
        print(e[0], '\t', e[1])

