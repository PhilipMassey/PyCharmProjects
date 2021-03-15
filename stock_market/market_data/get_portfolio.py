import pandas as pd
import market_data as md


def addPortfolioTodf_stock_old(df_stock):
    df_port = md.getPortfoliosAndSymbols()
    df_port.set_index('symbol', inplace=True)
    df_stock = pd.concat([df_stock, df_port], axis=1)
    return df_stock


def addPortfolioTodf_stock(df_stock):
    df_stock = df_stock.reset_index().rename(columns=({'index': 'symbol'}))
    df_port = md.getPortfoliosAndSymbols()
    return df_stock.merge(df_port)
