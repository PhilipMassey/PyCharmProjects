import requests
import pandas as pd
import json

def get_sa_screener_details_list():
    url = "https://seeking-alpha.p.rapidapi.com/screeners/list"

    headers = {
        'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
        'x-rapidapi-key': "b8e3f8e3c8msh1c3174e834acd9bp10bb99jsnba74a76fb55e"
        }

    response = requests.request("GET", url, headers=headers)

    response.text
    datas = json.loads(response.text)['data']
    alist = []
    for data in datas:
        name = data['attributes']['name']
        flter = data['attributes']['filters']
        alist.append((name,str(flter).replace("'",'"')))
    return alist