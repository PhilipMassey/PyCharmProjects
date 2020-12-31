import pandas as pd
import market_data as md

def getdfStockPortfolio(df_stock):
    df_port = md.getPortfolios()
    df_port.set_index('symbol',inplace=True)
    df_stock = pd.concat([df_stock,df_port],axis=1)
    return df_stock
