import requests
import pandas as pd
import json
import os
from os.path import join
import market_data as md
import apis as apis
perpage = 60

def change_value_to_list(dictionary):
    for key in dictionary:
        dictionary[key] = list(dictionary[key])

def get_energy_stocks():
    base = '/Users/philipmassey/PycharmProjects/stock_market'
    subdir = 'apis/seeking_alpha/screener_details_apis'
    fname= 'energy_stocks.csv'
    path = join(base, subdir, fname)
    df = pd.read_csv(path)
    df.rename(columns={'Ticker':'symbol'},inplace=True)
    return list(df.symbol.values)


def get_energy_symbols(resultsdict):
    esymbols = get_energy_stocks()
    energy_ports = ['Top Energy Stocks', 'Top Energy by SA Authors ']
    for eport in energy_ports:
        esymbols.extend(resultsdict[eport])
    return list(set(esymbols))


def remove_energy_stocks(resultsdict):
    esymbols = get_energy_symbols(resultsdict)
    for port in resultsdict.keys():
        remove_elements(resultsdict[port], esymbols)
    print('remove energy stocks')


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



def file_api_symbols(resultsdict, path):
    suffix = '.csv'
    for key in resultsdict.keys():
        tickers = resultsdict[key]
        fpath = os.path.join(path, key + suffix)
        with open(fpath, 'w') as f:
            f.write('Ticker\n' + '\n'.join(tickers))
            f.close()
    print('completed: updating ', path)

