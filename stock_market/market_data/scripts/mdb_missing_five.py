import sys; sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])
sys.path.extend(['/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages'])
import market_data as md

symbols = md.get_symbols(incl=md.all)

start = 0
end = 5
[md.update_mdb_with_missing_row(ndays, symbols) for ndays in range(start, end)]
start = 0
end = 3
[md.update_mdb_with_missing_row(ndays, symbols) for ndays in range(start, end)]
