import market_data as md
import pandas as pd


def get_percent_change_dfs(dfs, dfe):
    dfs.dropna(inplace=True, how='all');
    dfe.dropna(inplace=True, how='all')
    df_all = pd.concat([dfs, dfe])
    df_pc = df_all.pct_change(periods=1)
    df_pc = df_pc.iloc[1:]
    df_stock = df_pc.reset_index(drop=True, inplace=False).T.rename(columns={0: 'percent'}, inplace=False)
    df_stock['percent'] = df_stock['percent'].apply(lambda x: round(x * 100, 2))
    return df_stock


def df_percents_for_range(ndays_range, symbols='', incl='', ports=[]):
    if len(incl) > 0:
        symbols = md.get_symbols(incl)
    elif len(ports) > 0:
        symbols = md.get_symbols(ports=ports)
    elif len(symbols) == 0:
        symbols = md.get_symbols(directory=md.all)
    symbols = sorted(symbols)
    df_all = pd.DataFrame({})
    end_ndays = ndays_range[0]
    dfe = md.get_df_from_mdb_for_nday(end_ndays,md.db_test_close,symbols)
    for ndays in ndays_range[1:]:
        print(ndays)
        dfs = md.get_df_from_mdb_for_nday(ndays,md.db_test_close,symbols)
        dfp = get_percent_change_dfs(dfs,dfe)
        dfp[str(ndays) + ' days'] = dfp['percent']
        dfp.drop(columns=('percent'),inplace=True)
        df_all = pd.concat([df_all,dfp],axis=1)
    df_all.reset_index(inplace=True)
    df_all.rename(columns=({'index': 'symbol'}), inplace=True)
    return df_all


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
