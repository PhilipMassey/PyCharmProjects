import portfolio as pf
import market_data as md
import pandas as pd

def getTodaySymPortPercPeriods(period, interval):
    dfa = pd.DataFrame()
    for ndays in range(1, period, interval):
        start, end = md.getNDateAndToday(ndays)
        df, dt = pf.getSymbolPortPercentVol(start,end)
        df['date'] = md.getNBusDateFromNdays(ndays)
        df.reset_index(inplace = True)
        dfa = pd.concat([dfa,df])
    dfa.sort_values(by=['date', 'portfolio'], ascending=[False,True], inplace=True)
    dfa.dropna(inplace=True)
    return dfa

def getTodaySymPortPercPeriodsFltrd(period, interval, excl_vol=False, excl_low_vol=False):
    dfa = getTodaySymPortPercPeriods(period, interval)
    if excl_vol is True:
        symbols = md.getHighVolatilityStocks()
        dfa = dfa[~dfa.symbol.isin(symbols)]
    if excl_low_vol is True:
        symbols = md.getLowVolatilityStocks()
        dfa = dfa[~dfa.symbol.isin(symbols)]
    return dfa

def aggregateOnPortfolio(dfall):
    df = dfall.reset_index(drop=True)
    df.drop(columns=['symbol'], inplace=True)
    df = df.groupby(['date', 'portfolio']).agg(['mean'])
    df.columns = df.columns.get_level_values(0)
    df.reset_index(inplace=True)
    return df

def getPeriodIntervalSymPortPerc(period, interval):
    dfa = pd.DataFrame()
    for ndays in range(1, period, interval):
        end = md.getNBusDateFromNdays(ndays)
        start = md.getNBusDateFromNdays(ndays + interval)
        df, dt = pf.getSymbolPortPercentVol(start,end)
        df['date'] = md.getNBusDateFromNdays(ndays)
        df.reset_index(inplace = True)
        df = df.rename(columns={'index':'symbol'})
        dfa = pd.concat([dfa,df])
    dfa.sort_values(by=['date', 'portfolio'], ascending=[False,True], inplace=True)
    dfa.dropna(inplace=True)
    return dfa

def getPeriodIntervalSymPortPercFltrd(period, interval, excl_vol=False, excl_low_vol=False):
    dfa = getPeriodIntervalSymPortPerc(period, interval)
    if excl_vol is True:
        symbols = md.getHighVolatilityStocks()
        dfa = dfa[~dfa.symbol.isin(symbols)]
    if excl_low_vol is True:
        symbols = md.getLowVolatilityStocks()
        dfa = dfa[~dfa.symbol.isin(symbols)]
    return dfa
