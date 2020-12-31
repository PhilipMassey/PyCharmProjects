import portfolio as pf
import market_data as md
import pandas as pd

def getPortPercPeriods(period, interval,account):
    dfa = pd.DataFrame()
    for ndays in range(1,period,interval):
        dfg,dt = pf.getSymbolPortPercentVol(ndays, account)
        dfg = dfg.groupby('portfolio').agg(['mean'])
        dfg.columns = ['percent','volume']
        dfg.reset_index(inplace = True)
        dfg = dfg.rename(columns={'index':'portfolio'})
        dfg['date'] = md.getNBusDateFromNdays(ndays)
        dfa = pd.concat([dfa,dfg])
        dfa.sort_values(by=['date', 'portfolio'], ascending=[False, True], inplace=True)
    return dfa


def getSymPortPercPeriods(period,interval):
    dfa = pd.DataFrame()
    for ndays in range(1, period, interval):
        df, dt = pf.getSymbolPortPercentVol(ndays)
        df['date'] = md.getNBusDateFromNdays(ndays)
        df.reset_index(inplace = True)
        df = df.rename(columns={'index':'symbol'})
        dfa = pd.concat([dfa,df])
        dfa.sort_values(by=['date', 'portfolio'], ascending=[False,True], inplace=True)
    return dfa

def getSymPortPercPeriodsLowVty(period,interval,volatile=True):
    dfa = getSymPortPercPeriods(period,interval)
    if volatile is False:
        symbols = md.getVolatileStocks()
        dfa = dfa[~dfa.symbol.isin(symbols)]
    return dfa

def aggregateOnPortfolio(dfall):
    df = dfall.reset_index(drop=True)
    df.drop(columns=['symbol'], inplace=True)
    df = df.groupby(['date', 'portfolio']).agg(['mean'])
    df.columns = df.columns.get_level_values(0)
    df.reset_index(inplace=True)
    return df