import pandas as pd

def getPortfolios():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/portfolio_symbol.csv'
    df_port = pd.read_csv(path).set_index('symbol')
    return df_port

def getStockPickleDirectory():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/stock_pickles'
    return path

def getPickleName(rdate):
    ppath = getStockPickleDirectory()
    return ppath+'/'+rdate+'.pk'
