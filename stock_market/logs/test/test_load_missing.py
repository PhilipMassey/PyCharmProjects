import sys;sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])
import performance as pf
import market_data as md
import pandas as pd

incl = md.test
incl = md.all
symbols = md.get_symbols(incl)
symbols = ['TLT','EDV']
#print(symbols)
start = 5
end = 6
[md.update_mdb_with_missing_row(ndays, symbols) for ndays in range(start, end)]
