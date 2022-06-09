import market_data as md
import pandas as pd
import apis

def int_to_en(num):
    d = { 0 : 'zer', 1 : 'one', 2 : 'two', 3 : 'thr', 4 : 'fou', 5 : 'fiv',
          6 : 'six', 7 : 'sev', 8 : 'eig', 9 : 'nin', 10 : 'ten',
          11 : '11', 12 : '12', 13 : '13', 14 : '14',
          15 : '15', 16 : '16', 17 : '17', 18 : '18',
          19 : '19', 20 : '20', 21 : '21', 22: '22', 23 : '23',
         24:'24',25:'25',26:'26',27:'27',28:'28',29:'29',30:'30',
        31:'31',32:'32',33:'33',34:'34',35:'35',36:'36',37:'37',38:'38',
        39:'39',40:'40',41:'41',42:'42',43:'43',44:'44',45:'45',46:'46',47:'47',48:'48',49:'49',50:'50'}
    return d[num]

def holding_non_sa():
    holding = md.get_symbols('holding')
    sa_symbols = md.get_symbols('Seeking_Alpha')
    non_sa_symbols = sorted(set(holding).difference(set(sa_symbols)))
    non_sa_symbols
    long_term = md.get_symbols_for_portfolios(['Long Term','Solar, Semis, Water'])
    return sorted(set(non_sa_symbols).difference(set(long_term)))


def df_non_sa():
    non_sa_symbols = holding_non_sa()
    non_sa_symbols
    dfnsa = pd.DataFrame({'Non SA':non_sa_symbols})
    dfnsa =dfnsa.T
    dfnsa.columns = [int_to_en(column) for column in dfnsa.columns]
    dfnsa.reset_index(inplace=True)
    dfnsa.rename(columns={'index':'Portfolio'},inplace=True)
    return dfnsa


def df_symbols_by_sa_ports(symbols,directory='Holding'):
    sa_ports = md.sa_ports
    sa_ports.append(md.sc_port)
    dct = {}
    for port in sa_ports:
        quant = md.get_symbols_for_portfolios([port])
        symbolsx = sorted(set(symbols).intersection(set(quant)))
        #print(port, ': ', symbols)
        dct[port] = symbolsx
    df = pd.DataFrame.from_dict(dct, orient='index')
    df.columns = [int_to_en(column) for column in df.columns]
    df.reset_index(inplace=True)
    df.rename(columns={'index':'Portfolio'},inplace=True)
    if directory == 'Holding':
        df_non_sa_symbols = df_non_sa()
        df = pd.concat([df,df_non_sa_symbols])
    return df


def df_symbols_by_sector(symbols):
    fields = ['symbol','sectorname','primaryname']
    df = apis.df_symbol_profile(symbols, fields)
    df.dropna(inplace=True)
    dct = {}
    for sector in df.sectorname.values:
        dct[sector] = sorted(list(df[df.sectorname==sector].symbol.values))
    df =pd.DataFrame.from_dict(dct, orient='index')
    df
    df.columns = [int_to_en(column) for column in df.columns]
    df.reset_index(inplace=True)
    df.rename(columns={'index':'Sector'},inplace=True)
    return df.sort_values(by='Sector')


def df_symbols_by_portfolio(df_ports_symbols):
    df = df_ports_symbols
    dct = {}
    for port in df.portfolio.values:
        dct[port] = sorted(list(df[df.portfolio==port].symbol.values))

    df =pd.DataFrame.from_dict(dct, orient='index')
    df.columns = [int_to_en(column) for column in df.columns]
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Portfolio'}, inplace=True)
    return df

def reorder_cols(df):
    cols = list(df.columns)
    end = len(cols)-2
    rcols = cols[:end]
    ucols = [cols[-2],cols[-1]]
    ucols.extend(rcols)
    return df[ucols]


def df_symbols_by_sector_industry(symbols):
    fields = ['symbol','sectorname','primaryname']
    df = apis.df_symbol_profile(symbols, fields)
    df.dropna(inplace=True)
    dct = {}
    for sector in df.sectorname.values:
            for industry in df[df.sectorname==sector].primaryname.values:
                dct[(sector,industry)] = sorted(list(df[df.primaryname==industry].symbol.values))
    df =pd.DataFrame.from_dict(dct, orient='index')
    df.columns = [int_to_en(column) for column in df.columns]
    df['Sector'] = [l[0] for l in df.index.values]
    df['Industry'] = [l[1] for l in df.index.values]
    df.reset_index(inplace=True)
    df.drop(columns=['index'],inplace=True)
    df.sort_values(by='Sector',inplace=True)
    df = reorder_cols(df)
    return df
