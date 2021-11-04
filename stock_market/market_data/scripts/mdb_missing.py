import sys
sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])
sys.path.extend(['/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages'])
import market_data as md

incl = md.all
start = 1
end = 10  # end = 180
symbols = md.get_symbols(incl)
#symbols = ['TLT','EDV']
for ndays in range(start, end):
    symbols = md.update_mdb_with_missing_row(ndays, symbols)
    print()

    # [md.update_mdb_with_missing_row(ndays, incl) for ndays in range(start, end)]
