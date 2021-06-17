import pandas as pd
import market_data as md

def addPortfolioTodf_stock(df_stock,incl):
    df_stock = df_stock.reset_index().rename(columns=({'index': 'symbol'}))
    df_port = md.get_port_and_symbols(incl)
    return df_stock.merge(df_port)

def get_df_symbol_portfolios(symbols):
    df = pd.DataFrame({})
    df['symbol'] = symbols
    df_port = md.get_port_and_symbols(incl=md.all)
    return df.merge(df_port).sort_values(by=['portfolio'])
