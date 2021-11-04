import performance as pf
import market_data as md
import pandas as pd

def df_percents_for_range(ndays_range, symbols='', incl='', port=[]):
    if len(incl) > 0:
        symbols = md.get_symbols(incl)
    elif len(port) > 0:
        symbols = md.get_symbols(port=port)
    elif len(symbols) == 0:
        symbols = md.get_symbols(incl=md.all)
    symbols = sorted(symbols)
    dfAll = pd.DataFrame({})
    end_ndays = 1
    df1 = md.get_df_from_mdb_for_nday(end_ndays,md.db_close,symbols)
    for ndays in ndays_range:
        dfe = md.get_df_from_mdb_for_nday(ndays,md.db_close,symbols)
        dfp = pf.get_percent_change_dfs(dfe,df1)
        dfp[str(ndays) + ' days'] = dfp['percent']
        dfp.drop(columns=('percent'),inplace=True)
        dfAll = pd.concat([dfAll,dfp],axis=1)
    dfAll.reset_index(inplace=True)
    dfAll.rename(columns=({'index': 'symbol'}), inplace=True)
    return dfAll

def getTodaySymPortPercPeriods(period_interval,incl):
    period,interval = period_interval
    dfa = pd.DataFrame()
    for ndays in range(0, period, interval):
        start, end = md.get_dates_ndays_and_today(ndays)
        #print(start,end)
        df, dt = pf.get_symbol_port_perc_vol(start, end, incl)
        df['date'] = md.getNBusDateFromNdays(ndays)
        df.reset_index(inplace = True)
        dfa = pd.concat([dfa,df])
    dfa.sort_values(by=['date', 'portfolio'], ascending=[False,True], inplace=True)
    dfa.dropna(inplace=True)
    return dfa

def getTodaySymPortPercPeriodsFltrd(period_interval, incl,excl=True):
    dfa = getTodaySymPortPercPeriods(period_interval,incl)
    if excl is True:
        symbols = md.getHighVolatilityStocks()
        dfa = dfa[~dfa.symbol.isin(symbols)]
    return dfa


def getPrevDaySymPortPercPeriods(nstart,period_interval,incl):
    period,interval = period_interval
    period += nstart
    dfa = pd.DataFrame()
    for ndays in range(nstart, period, interval):
        start, end = md.getNDateAndPrevDate(ndays, interval)
        df, dt = pf.get_symbol_port_perc_vol(start, end, incl)
        df['date'] = md.getNBusDateFromNdays(ndays)
        df.reset_index(inplace = True)
        dfa = pd.concat([dfa,df])
    dfa.sort_values(by=['date', 'portfolio'], ascending=[False,True], inplace=True)
    dfa.dropna(inplace=True)
    return dfa


def getPrevDaySymPortPercPeriodsFltrd(nstart, period, interval, incl, excl=True):
    dfa = getPrevDaySymPortPercPeriods(nstart,period,interval,incl)
    if excl is True:
        symbols = md.getHighVolatilityStocks()
        dfa = dfa[~dfa.symbol.isin(symbols)]
    return dfa

def aggregateOnPortfolio(dfall):
    df = dfall.reset_index(drop=True)
    df.drop(columns=['symbol'], inplace=True)
    df = df.groupby(['date', 'portfolio']).agg(['mean'])
    df.columns = df.columns.get_level_values(0)
    df.reset_index(inplace=True)
    return df
