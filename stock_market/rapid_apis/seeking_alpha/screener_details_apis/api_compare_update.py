import requests
import pandas as pd
import json
import os
from os.path import join
import market_data as md
import rapid_apis as sa_apis


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


def trim_to_count(resultsdict,count):
    for port in resultsdict.keys():
        if port not in eports:
            resultsdict[port] = resultsdict[port][:count]


def compare_old_new(resultsdict):
    oldnew_dict = {}
    for port in resultsdict.keys():
        new_symbols = resultsdict[port]
        current_symbols = md.get_symbols(ports=[port])
        oldnew_dict[port] = {'old': set(current_symbols).difference(set(new_symbols)),
                             'new': set(new_symbols).difference(set(current_symbols))}
    return oldnew_dict

def write_oldnew_dict(oldnew_dict,fpath_name):
    with open(fpath_name, 'w') as f:
        for key in oldnew_dict.keys():
            f.write(key + '\n')
            f.write('\t' + str(oldnew_dict[key]['old']) + '\n')
            f.write('\t' + str(oldnew_dict[key]['new']) + '\n')
        f.close()
    print('writen old/new comparison: ', path)


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
    resultsdict = sa_apis.adict_screener_details(screeners, 20)

    replacedot((resultsdict))
    remove_energy_stocks(resultsdict)
    trim_to_count(resultsdict,10)

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

