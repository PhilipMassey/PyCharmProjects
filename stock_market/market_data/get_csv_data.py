import pandas as pd
import os
from os.path import isfile, join, isdir
from os import listdir

import market_data as md

def portfolio_from_file(subdir,file):
    path = join(md.data_dir, subdir, file)
    df = pd.read_csv(path)
    fname = file[0:-4]
    df['portfolio'] = fname
    df.rename(columns={'Ticker':'symbol'},inplace=True)
    return df

def get_dir_port_symbols(subdir):
    path = os.path.join(md.data_dir, subdir)
    csv_files = [f for f in listdir(path) if isfile(join(path, f))]
    dfall = pd.DataFrame(columns=('portfolio', 'symbol'))
    for file in csv_files:
        dfall = pd.concat([dfall, portfolio_from_file(subdir, file)], axis=0)
    dfall.reset_index(drop=True, inplace=True)
    return dfall

def get_port_and_symbols(incl):
    df_all = pd.DataFrame(columns=('portfolio','symbol'))
    if incl == md.all:
        dirs = [d for d in listdir(md.data_dir) if isdir(join(md.data_dir, d))]
        for dir in dirs:
            df = get_dir_port_symbols(dir)
            df_all = pd.concat([df_all, df], axis=0)
    else:
        df = get_dir_port_symbols(incl)
        df_all = pd.concat([df_all, df], axis=0)
    # elif incl == md.watching:
    #     df = get_dir_port_symbols(md.watching)
    #     df_all =  pd.concat([df_all, df],axis=0)
    # elif incl == md.ark:
    #     df = get_dir_port_symbols(md.ark)
    #     df_all = pd.concat([df_all,df])
    # elif incl == md.etf:
    #     df = get_dir_port_symbols(md.etf)
    #     df_all = pd.concat([df_all,df])
    # elif incl == md.test:
    #     df = get_dir_port_symbols(md.test)
    #     df_all = df
    return df_all

def getPortfolios(incl):
    df_port = get_port_and_symbols(incl)
    return set(df_port.portfolio.values)

def get_symbols(incl):
    df = get_port_and_symbols(incl)
    return list(set(df.symbol.values))

def getPortfoliosSymbols(portfolios):
    port_symbols = get_port_and_symbols()
    return port_symbols[port_symbols.portfolio.isin(portfolios)].symbol.values

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

def getFidelitySymbols():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/data/fidelity.csv'
    df_fidelity = pd.read_csv(path).set_index('symbol')
    symbols = list(df_fidelity.index.values)
    return symbols



