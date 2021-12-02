import market_data as md
import pandas as pd

def get_percent_change_dfs(dfs, dfe):
    dfs.dropna(inplace=True, how='all');dfe.dropna(inplace=True, how='all')
    dfAll = pd.concat([dfs, dfe])
    df_pc = dfAll.pct_change(periods=1)
    df_pc = df_pc.iloc[1:]
    df_stock = df_pc.reset_index(drop=True, inplace=False).T.rename(columns = {0:'percent'}, inplace = False)
    df_stock['percent'] = df_stock['percent'].apply(lambda x:round(x*100,2))
    return df_stock

def get_stock_vol(dfVol):
    df_vol = dfVol.iloc[:1].reset_index(drop=True, inplace=False).T.rename(columns = {0: 'volume'}, inplace = False)
    return df_vol['volume']

def get_symbol_port_perc_vol(start, end, incl):
    dfCloseStart, dfVolStart = md.get_mdb_rows_close_vol(start, incl)
    dfCloseEnd, dfVolEnd = md.get_mdb_rows_close_vol(end, incl)
    df_stock = get_percent_change(dfCloseStart, dfCloseEnd)
    df_stock['volume'] = get_stock_vol(dfVolEnd)
    df_stock = md.add_portfolio_to_df_stock(df_stock,incl)
    endDt = md.getDescriptiveDate(dfCloseEnd)
    return df_stock, endDt

