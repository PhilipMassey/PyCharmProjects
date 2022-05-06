import requests
import pandas as pd
import json
import os
import market_data as md
import rapid_apis as ra_apis
subdir = 'Seeking_Alpha'
suffix = '.csv'


def get_sa_screener_details_list():
    url = "https://seeking-alpha.p.rapidapi.com/screeners/list"

    headers = {
        'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
        'x-rapidapi-key': ra_apis.seeking_alpha_key
    }

    response = requests.request("GET", url, headers=headers)

    response.text
    datas = json.loads(response.text)['data']
    alist = []
    for data in datas:
        name = data['attributes']['name']
        flter = data['attributes']['filters']
        alist.append((name, str(flter).replace("'", '"')))
    return alist

def adict_screener_details(screeners, perpage):
    url = "https://seeking-alpha.p.rapidapi.com/screeners/get-results"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
        'x-rapidapi-key': "b8e3f8e3c8msh1c3174e834acd9bp10bb99jsnba74a76fb55e"
    }
    querystring = {"page": "1", "per_page": "" + str(perpage) + ""}

    adict = {}
    for screener in screeners:
        print(screener[0],end=',')
        fname = screener[0]
        payload = screener[1].replace(', "disabled": False','')
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        data = response.text
        if str(data) == '400 - Bad Request' or 'error' in str(data):
            print(data)
            print(screener[0], screener[1])
        else:
            df = pd.json_normalize(json.loads(data)['data'])
            tickers = df['attributes.name'].values
            adict[fname] = tickers
    return adict