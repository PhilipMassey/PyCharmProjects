import pandas as pd
import market_data as md

def add_portfolio_to_df_stock(df_stock, incl):
    df_stock = df_stock.reset_index().rename(columns=({'index': 'symbol'}))
    df_port = md.get_port_and_symbols(incl)
    return df_stock.merge(df_port)

def get_df_symbol_portfolios(symbols):
    df = pd.DataFrame({})
    df['symbol'] = symbols
    df_port = md.get_port_and_symbols(incl=md.all)
    return df.merge(df_port).sort_values(by=['portfolio'])

def index_to_column(df, column):
    df = df.reset_index().rename(columns=({'index':column}))
    return df.sort_values(by=[column])