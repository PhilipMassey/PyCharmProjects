import requests
import json
import http.client
import market_data as md
import pandas as pd

conn = http.client.HTTPSConnection("seeking-alpha.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
    'x-rapidapi-key': "b8e3f8e3c8msh1c3174e834acd9bp10bb99jsnba74a76fb55e"
    }


def dct_symbol_name(symbols):
    dct_symb_name = {}
    for idx in range(0,len(symbols),4):
        symbols4= "%2C".join(symbols[idx:idx+4])

        conn.request("GET", "/symbols/get-profile?symbols=" + symbols4, headers=headers)

        res = conn.getresponse()
        data = res.read()
        txt = data.decode("utf-8")
        if 'data' not in txt:
            print('No data ',symbols)
            continue
        ldcts = json.loads(txt)['data']
        for idx in range(len(ldcts)):
            if ldcts[idx]['attributes']['etfName']:
                #print(ldcts[idx]['id'],ldcts[idx]['attributes']['etfName'])
                dct_symb_name[ldcts[idx]['id']] = ldcts[idx]['attributes']['etfName']
            else:
                #print(ldcts[idx]['id'],ldcts[idx]['attributes']['quoteName'])
                dct_symb_name[ldcts[idx]['id']] = ldcts[idx]['attributes']['quoteName']
    return dct_symb_name


def mdb_add_symbols_names_directory(directory):
    ports = md.get_ports_for_directory(directory)
    mdb_symbols = md.mdb_profile_get_symbols()
    #print(mdb_symbols)
    for port in ports:
        print('\t',port, end=': ')
        symbols = md.get_symbols(ports=[port])
        not_added_symbols = set(symbols).difference(set(mdb_symbols))
        print(len(not_added_symbols))
        if len(not_added_symbols) > 0:
            print('not added symbols: ', not_added_symbols)
            symbol_name_dct = dct_symbol_name(list(not_added_symbols))
            data = {'symbol': symbol_name_dct.keys(), 'name': symbol_name_dct.values()}
            result = md.add_dct_to_mdb(data, md.db_symbol_profile)
            #print(result)
            mdb_symbols.extend(not_added_symbols)

dirs = md.get_directorys()
for directory in dirs:
    print('Directory: ',directory)
    mdb_add_symbols_names_directory(directory)
