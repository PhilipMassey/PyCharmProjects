import requests
import pandas as pd
import market_data as md
import apis

key_data_fields = ['eps','peRatioFwd','estimateEps','divYield','marketCap','volume','evEbit','evEbitda','evFcf','evSales','fcf','fcfShare','marketCap','movAvg10d','movAvg10w','movAvg200d','payout4y','payoutRatio','pegRatio','peRatioFwd','priceBook','priceCf','priceSales','priceTangb','quickRatio','revenueGrowth','revenueGrowth3','revPShare','revToAssets','roa','roe','shares','ltDebtCap']

key_data_url = "https://seeking-alpha.p.rapidapi.com/symbols/get-key-data"
key_data_headers = {
    'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
    'x-rapidapi-key': md.seeking_alpha_key
    }


def df_symbol_key_data(symbol,key_data_fields):
    symbol = symbol.upper()
    querystring = {'symbol':symbol}
    response = requests.request("GET", key_data_url, headers=key_data_headers, params=querystring)
    symbol_dct = response.json()['data'][0]
    dct_attribs =symbol_dct['attributes']
    symbol_fields ={}
    keys = dct_attribs.keys()
    for field in key_data_fields:
        if field in keys:
            symbol_fields[field] = dct_attribs[field]
    df = pd.DataFrame.from_dict(symbol_fields, orient='index',columns=[symbol] )
    df = df.T.reset_index().rename(columns={'index':'symbol'})
    return df

summary_fields = ['shortIntPctFloat','peRatioFwd','estimateEps','divYield','marketCap','volume','evEbit','evEbitda','evFcf','evSales','fcf','fcfShare','marketCap','movAvg10d','movAvg10w','movAvg200d','payout4y','payoutRatio','pegRatio','peRatioFwd','priceBook','priceCf','priceSales','priceTangb','quickRatio','revenueGrowth','revenueGrowth3','revPShare','revToAssets','roa','roe','shares','ltDebtCap']

summary_url = "https://seeking-alpha.p.rapidapi.com/symbols/get-summary"

summary_headers = {
    'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
    'x-rapidapi-key':  md.seeking_alpha_key
    }

def df_symbol_summary_fields(symbol,summary_fields):
    symbol = symbol.upper()
    querystring = {'symbols':symbol}
    response = requests.request("GET", summary_url, headers=summary_headers, params=querystring)
    dctall = response.json()['data']
    for idx in range(len(dctall)):
        symbol_dct = dctall[idx]
        symbol_info = {}
        #symbol = symbol_dct['id']
        dct_attribs =symbol_dct['attributes']
        keys = dct_attribs.keys()
        symbol_fields ={}
        for field in summary_fields:
            if field in keys:
                symbol_fields[field] = dct_attribs[field]
        df = pd.DataFrame.from_dict(symbol_fields, orient='index',columns=[symbol] )
        df = df.T.reset_index().rename(columns={'index':'symbol'})
        return df

def df_symbol_info(ndays, symbol):
    symbol = symbol.upper()
    dfs = apis.df_symbol_summary_fields(symbol, summary_fields)
    dfk = apis.df_symbol_key_data(symbol, key_data_fields)
    df = pd.concat([dfs, dfk], axis=1)
    df = df.T.drop_duplicates().T
    md.df_add_date_index(ndays, df)
    return df

