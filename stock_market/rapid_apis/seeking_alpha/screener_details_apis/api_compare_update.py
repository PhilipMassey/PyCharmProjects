import requests
import pandas as pd
import json
import os
from os.path import join
import market_data as md
import rapid_apis as sa_apis


def change_value_to_list(dictionary):
    for key in dictionary:
        dictionary[key] = list(dictionary[key])


def get_energy_symbols(resultsdict):
    energy_ports = ['Top Energy Stocks', 'Top Energy by SA Authors ']
    esymbols = []
    for eport in energy_ports:
        esymbols.extend(resultsdict[eport])
    esymbols = list(set(esymbols))
    return esymbols


def remove_energy_stocks(resultsdict):
    esymbols = get_energy_symbols(resultsdict)
    for port in resultsdict.keys():
        ra_apis.remove_elements(resultsdict[port], esymbols)
    print('remove energy stocks')


def build_dict_count(screeners, default_count = 15):
    screener_names = [screener[0] for screener in screeners]
    dict_count ={}
    for name in screener_names:
        dict_count[name] = default_count
    dict_count['Top Rated Stocks'] = 30
    dict_count['Top Stocks by Quant'] = 30
    dict_count['Top Energy Stocks'] = 0
    dict_count['Top Energy by SA Authors '] = 0
    dict_count['Most Shorted Stocks'] = 0
    dict_count['Strong Buy Stocks With Short Squeeze Potential'] = 0
    return dict_count


def trim_to_count(resultsdict, dict_count):
    for port in resultsdict.keys():
        trim = dict_count[port]
        resultsdict[port] = resultsdict[port][:trim]
    print('trimmed resultsdict')


def remove_elements(alist, elements):
    for el in elements:
        if el in alist:
            alist.remove(el)

def replacedot(resultsdict):
    for port in resultsdict:
        listtickers = resultsdict[port]
        newtickers = []
        for ticker in listtickers:
            newtickers.append(ticker.replace(".",'-'))
        resultsdict[port] = newtickers


def file_api_symbols(resultsdict, subdir, suffix):
    for key in resultsdict.keys():
        tickers = resultsdict[key]
        path = os.path.join(md.data_dir, subdir, key + suffix)
        with open(path, 'w') as f:
            f.write('Ticker\n' + '\n'.join(tickers))
            f.close()
        print('updated: ', key)
    print('completed: updating ', subdir)


if __name__ == '__main__':
    screeners = sa_apis.get_sa_screener_details_list()
    for idx in range(len(screeners)):
        screener = screeners[idx]
        print(idx, screener[0])
    resultsdict = adict_screener_details(screeners, perpage=45)
    change_value_to_list(resultsdict)
    remove_energy_stocks(resultsdict)
    replacedot((resultsdict))
    dict_count = build_dict_count(screeners)
    trim_to_count(resultsdict, dict_count)

    oldnew_dict = compare_old_new(resultsdict)

    home = '/Users/philipmassey/'
    subdir = 'Downloads'
    fname = 'SA rapid api update'
    suffix = '.txt'
    fpath_name = os.path.join(home,sudir,fname,suffix)
    write_oldnew_dict(oldnew_dict, fpath_name)

    subdir = 'Seeking_Alpha'
    suffix = '.csv'
    file_api_symbols(resultsdict, subdir, suffix)

