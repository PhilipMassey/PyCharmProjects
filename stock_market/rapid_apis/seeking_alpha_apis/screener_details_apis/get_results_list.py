import requests
import pandas as pd
import json
import os
import market_data as md

subdir = 'Seeking_Alpha'
suffix = '.csv'

url = "https://seeking-alpha.p.rapidapi.com/screeners/get-results"
headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
    'x-rapidapi-key': "b8e3f8e3c8msh1c3174e834acd9bp10bb99jsnba74a76fb55e"
    }

querystring = {"page":"1","per_page":"20"}

def get_sa_screener_details_list():

    response = requests.request("GET", url, headers=headers)

    response.text
    datas = json.loads(response.text)['data']
    alist = []
    for data in datas:
        name = data['attributes']['name']
        flter = data['attributes']['filters']
        alist.append((name,str(flter).replace("'",'"')))
    return alist


def replacedot(listtickers):
    newtickers = []
    for ticker in listtickers:
        newtickers.append(ticker.replace(".",'-'))
    return newtickers


def adict_screener_details(screeners, count=12):
    adict = {}
    for screener in screeners:
        fname = screener[0]
        payload = screener[1].replace(', "disabled": False','')
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        data = response.text
        if str(data) == '400 - Bad Request':
            print(data)
            print(screener[0], screener[1])
        else:
            df = pd.json_normalize(json.loads(data)['data'])
            tickers = df['attributes.name'].head(count).values
            tickers = replacedot(list(tickers))
            adict[fname] = tickers
    return adict



# def file_screener_details(subdir, url, headers):
#     screeners = get_sa_screener_details_list()
#     for screener in screeners:
#         fname = screener[0]
#         payload = screener[1]
#         response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
#
#         data = response.text
#         if str(data)== '400 - Bad Request':
#             print(data)
#             print(screener[0], screener[1])
#         else:
#             df = pd.json_normalize(json.loads(data)['data'])
#             tickers = df['attributes.name'].head(12).values
#             tickers = replacedot(list(tickers))
#             #print(tickers)
#             path = os.path.join(md.data_dir, subdir,fname+suffix)
#             with open(path, 'w') as f:
#                 f.write('Ticker\n'+'\n'.join(tickers))
#                 f.close()
#     print('completed')

