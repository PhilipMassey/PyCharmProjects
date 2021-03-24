import pandas as pd

homedir = '/Users/philipmassey/PycharmProjects/stock_market/market_data/data/'

def getdfPortfolioSymbol(cvsfile):
    path = homedir+cvsfile+'.csv'
    df = pd.read_csv(path)
    return df


def getPortfoliosAndSymbols():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/data/portfolio_symbol.csv'
    df_port = pd.read_csv(path)
    return df_port

def getPortfolios():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/data/portfolio_symbol.csv'
    df_port = pd.read_csv(path)
    return set(df_port.portfolio)


def getAllPortfoliosSymbols():
    df_port = getPortfoliosAndSymbols()
    return list(df_port.symbol.values)

def getPortfolioSymbols(portfolio):
    port_symbols = getPortfoliosAndSymbols()
    return port_symbols[port_symbols.portfolio == portfolio].symbol.values

def getTradingPortfoliosSymbols(trading):
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/data/'+trading+'.csv'
    dfs = pd.read_csv(path)
    dfp = getPortfoliosAndSymbols()
    symbols = dfp[dfp.portfolio.isin(dfs.portfolio.values)].symbol.values
    portfolios = dfp[dfp.portfolio.isin(dfs.portfolio.values)].portfolio.unique()
    return (portfolios,symbols)

def getFidelitySymbols():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/data/fidelity.csv'
    df_fidelity = pd.read_csv(path).set_index('symbol')
    symbols = list(df_fidelity.index.values)
    return symbols

def getHighVolatilityStocks():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/data/volatile_stock.csv'
    df = pd.read_csv(path).set_index('symbol')
    symbols = list(df.index.values)
    return symbols

def getLowVolatilityStocks():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/data/low_vol_stocks.csv'
    df = pd.read_csv(path).set_index('symbol')
    symbols = list(df.index.values)
    return symbols
