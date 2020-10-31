import pandas as pd

def getPortfolios():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/portfolio_symbol.csv'
    df_portfolios = pd.read_csv(path).set_index('symbol')
    return df_portfolios

def getPortfoliosSymbols():
    df_port = pf.getPortfolios()
    symbols = list(df_port.index.values)
    return symbols