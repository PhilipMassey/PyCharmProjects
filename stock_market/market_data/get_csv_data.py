import pandas as pd

def getPortfolios():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/portfolio_symbol.csv'
    df_port = pd.read_csv(path)
    return df_port

def getTradingPortfoliosSymbols(trading):
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/'+trading+'.csv'
    dfs = pd.read_csv(path)
    dfp = getPortfolios()
    symbols = dfp[dfp.portfolio.isin(dfs.portfolio.values)].symbol.values
    portfolios = dfp[dfp.portfolio.isin(dfs.portfolio.values)].portfolio.unique()
    return (portfolios,symbols)

def getFidelitySymbols():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/fidelity.csv'
    df_fidelity = pd.read_csv(path).set_index('symbol')
    symbols = list(df_fidelity.index.values)
    return symbols

def getSchwabSymbols():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/schwab.csv'
    df_fidelity = pd.read_csv(path).set_index('symbol')
    symbols = list(df_fidelity.index.values)
    return symbols

def getVolatileStocks():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/alternative_medicine.csv'
    df = pd.read_csv(path).set_index('symbol')
    symbols = list(df.index.values)
    return symbols

def getPortfoliosSymbols():
    df_port = getPortfolios()
    return list(df_port.symbol.values)

