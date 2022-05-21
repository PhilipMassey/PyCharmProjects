import requests
import pandas as pd
import market_data as md

fields = ['shortIntPctFloat','peRatioFwd','estimateEps','divYield','marketCap','volume','evEbit','evEbitda','evFcf','evSales','fcf','fcfShare','marketCap','movAvg10d','movAvg10w','movAvg200d','payout4y','payoutRatio','pegRatio','peRatioFwd','priceBook','priceCf','priceSales','priceTangb','quickRatio','revenueGrowth','revenueGrowth3','revPShare','revToAssets','roa','roe','shares','ltDebtCap']
url = "https://seeking-alpha.p.rapidapi.com/symbols/get-summary"

#querystring = {"symbols":"veru,zim,egle,aapl,gogl,lxu,teck,mos"}
querystring = {'symbols':symbol}

headers = {
    'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
    'x-rapidapi-key': "b8e3f8e3c8msh1c3174e834acd9bp10bb99jsnba74a76fb55e"
    }
def df_symbol_details(symbol):
    querystring = {'symbols':symbol}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data =response.json()['data'][0]['attributes']
    dct = {}
    for field in fields:
        if field in data:
            dct[field] = data[field]
    dct
    df = pd.DataFrame.from_dict(dct, orient='index',columns=[symbol] )
    df = df.T.reset_index().rename(columns={'index':'symbol'})
    return df
df_symbol_details(symbol)