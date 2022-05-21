import market_data as md
import apis
from json import JSONDecodeError

def mdb_add_symbol_info_for_symbols(ndays, period, symbols,db_coll_name):
    total_symbols = len(symbols)
    update_count = 0
    skipped = 0
    error_count = 0
    for symbol in symbols:
        try:
            count = md.count_mdb_symbol_detween_dates(ndays, period, symbol, db_coll_name)
            if count == 0:
                print('+', end='')
                df = apis.df_symbol_info(ndays, symbol)
                md.add_symbol_info_mdb(ndays, period, symbol, df, db_coll_name)
                update_count += 1
            else:
                skipped += 1
                print('>', end=',')
        except (JSONDecodeError,KeyError) as e:
            print('\n',e, symbol)
            error_count += 1

    print('\nOf',total_symbols, '+', update_count, '>',skipped)
    if error_count > 0:
        print('errors',error_count)
    

if __name__ == '__main__':
    symbols = md.get_symbols('ETF')
    db_coll_name = 'symbol_info'
    ndays = 0
    period = 10
    mdb_add_symbol_info_for_symbols(ndays, period, symbols,db_coll_name)