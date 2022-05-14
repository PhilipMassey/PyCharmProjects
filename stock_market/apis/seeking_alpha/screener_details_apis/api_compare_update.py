import requests
import pandas as pd
import json
import os
from os.path import join
import market_data as md
import apis as ra_apis


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
        remove_elements(resultsdict[port], esymbols)
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

holding_ports =['SA Technology', 'SA Health, Industrial', 'Fidelity Potential', 'SA Industiral']

def get_old_holding_symbols(resultsdict):
    holding_symbols = set(md.get_symbols('',ports=holding_ports))
    stock_card = md.get_symbols_for_portfolios(['Stock Card Value and Momentum'])
    api_symbols = [*resultsdict.values()]
    api_symbols = set([item for sublist in api_symbols for item in sublist])
    old_symbols = holding_symbols - api_symbols
    for symbol in sorted(old_symbols):
        print(symbol,end=', ')

def get_old_sa_symbols(resultsdict):
    sa_directory = md.get_symbols_dir_or_port('Seeking_Alpha',None)
    stock_card = md.get_symbols_for_portfolios(['Stock Card Value and Momentum'])
    sa_symbols = set(sa_directory) - set(stock_card)
    api_symbols = [*resultsdict.values()]
    api_symbols = set([item for sublist in api_symbols for item in sublist])
    old_symbols = sa_symbols - api_symbols
    print('Seeking Aplha symbols downgraded in api')
    for symbol in sorted(old_symbols):
        print(symbol,end=', ')

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
    screeners = ra_apis.get_sa_screener_details_list()
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
    get_old_sa_symbols(resultsdict)
    get_old_holding_symbols(resultsdict)
    subdir = 'Seeking_Alpha'
    suffix = '.csv'
    file_api_symbols(resultsdict, subdir, suffix)

