import pandas as pd
import market_data as md

def getPortfolios():
    return md.getPortfolios()

def getPortfoliosSymbols():
    df_port = getPortfolios()
    return list(df_port.index.values)

