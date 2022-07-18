import market_data as md
import pandas as pd


def l_get_symbol_port_pos(symbol):
    dfs = ''
    directory = 'Seeking_Alpha'
    df_ports_syms = md.get_port_and_symbols(directory)
    sym_ports = df_ports_syms[df_ports_syms['symbol']==symbol].portfolio.values
    #s = pd.Series()
    s = []
    for port in sym_ports:
        port_symbols = md.get_symbols('',ports=[port])
        s.append((port,port_symbols.index(symbol)))
    return s


def df_sym_port_pos(portfolio):
    symbols = md.get_symbols('',ports=[portfolio])
    dfall = pd.DataFrame({})
    for symbol in symbols:
        sym_port_pos = l_get_symbol_port_pos(symbol)
        sym_port_pos_pad = ['' for sub in sym_port_pos]
        if len(sym_port_pos_pad) > 0:
            sym_port_pos_pad[0] = symbol
            df = pd.DataFrame({'Symbol':sym_port_pos_pad,'Portfolio':sym_port_pos})
        else:
            df = pd.DataFrame({'Symbol':[symbol],'Portfolio':[""]})
        dfall = pd.concat([dfall,df],ignore_index=True)
    return dfall


def df_directory_sym_port_pos(directory):
    ports = md.get_portfolios(directory)
    dfall = pd.DataFrame({})
    for port in ports:
        df = df_sym_port_pos(port)
        dfall = pd.concat([dfall,df],ignore_index=True)
    return dfall

def print_directory_sym_port_pos(directory):
    ports = md.get_portfolios(directory)
    for port in ports:
        print(port,'\n')
        df = df_sym_port_pos(port)
        print(df)

if __name__ == "__main__":
    directory = 'Holding'
    print_directory_sym_port_pos(directory)