import sys; sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])
sys.path.extend(['/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages'])
import market_data as md

print('{} missing'.format(md.ark))
symbols = md.get_symbols(incl=md.ark)
start = 0
end = 30
[md.update_mdb_with_missing_row(ndays, symbols) for ndays in range(start, end)]

print('{} missing'.format(md.etf))
symbols = md.get_symbols(incl=md.etf)
start = 0
end = 30
[md.update_mdb_with_missing_row(ndays, symbols) for ndays in range(start, end)]
