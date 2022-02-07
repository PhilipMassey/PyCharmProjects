import requests
import pandas as pd
import json
import os
import market_data as md
from rapid_apis import seeking_alpha_apis as sa_apis

eports = ['Top Energy Stocks', 'Top Energy by SA Authors ']


def get_esymbols(dict_api_symbols, eports):
    esymbols = []
    for eport in eports:
        esymbols.extend(dict_api_symbols[eport])
        esymbols.extend(md.get_symbols_for_portfolios([eport]))
    return set(esymbols)


def remove_elements(alist, elements):
    for el in elements:
        if el in alist:
            alist.remove(el)


def get_api_symbols_oldnew(count):
    oldnew_dict = {}
    screeners = sa_apis.get_sa_screener_details_list()
    dict_api_symbols = sa_apis.adict_screener_details(screeners, count)
    esymbols = get_esymbols(dict_api_symbols, eports)
    for port in dict_api_symbols.keys():
        current_symbols = md.get_symbols_for_portfolios([port])
        api_symbols = dict_api_symbols[port]
        remove_elements(api_symbols, esymbols)
        remove_elements(current_symbols, esymbols)
        oldnew_dict[port] = {'old': set(current_symbols).difference(set(api_symbols)),
                             'new': set(api_symbols).difference(set(current_symbols))}
    return dict_api_symbols, oldnew_dict


def write_oldnew_dict(oldnew_dict, fname, suffix):
    path = os.path.join(md.data_dir, subdir, fname + suffix)
    path = os.path.join(home, subdir, fname + suffix)
    with open(path, 'w') as f:
        for key in oldnew_dict.keys():
            f.write(key + '\n')
            f.write('\t' + str(oldnew_dict[key]['old']) + '\n')
            f.write('\t' + str(oldnew_dict[key]['new']) + '\n')
        f.close()
    print('writen old/new comparison: ', path)


def file_api_symbols(api_symbols, subdir, suffix):
    for key in api_symbols.keys():
        tickers = api_symbols[key]
        tickers = sa_apis.replacedot(list(tickers))
        path = os.path.join(md.data_dir, subdir, key + suffix)
        with open(path, 'w') as f:
            f.write('Ticker\n' + '\n'.join(tickers))
            f.close()
        print('updated: ', key)
    print('completed: updating ', subdir)


if __name__ == '__main__':
    dict_api_symbols, oldnew_dict = get_api_symbols_oldnew(12)

    home = '/Users/philipmassey/'
    subdir = 'Downloads'
    fname = 'SA rapid api update'
    suffix = '.txt'
    write_oldnew_dict(oldnew_dict, fname, suffix)


    subdir = 'Seeking_Alpha'
    suffix = '.csv'

    file_api_symbols(dict_api_symbols, subdir, suffix)

