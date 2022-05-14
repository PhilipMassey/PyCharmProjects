import requests
import json
import pandas as pd
import market_data as md
import apis as ra_apis

url = "https://seeking-alpha.p.rapidapi.com/v2/auto-complete"

headers = {
    'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
    'x-rapidapi-key': ra_apis.seeking_alpha_key
    }

def get_symbol_name(symbol):
    querystring = {"query": symbol,"type":"people,symbols,pages","size":"5"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    dt = json.loads(response.text)
    return dt['symbols'][0]['content']

symbol = 'ENPH'
name = get_symbol_name(symbol)

#print(symbol,name)
def dct_get_symbols_names(symbols):
    dct = {}
    for symbol in symbols:
        dct[symbol] = get_symbol_name(symbol)
    return dct


symbols = md.get_symbols(ports=['Bonds'])
dct = dct_get_symbols_names(symbols)
print(dct)