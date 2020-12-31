import market_data as md
import pandas as pd

def getStockPercentVol(dfEnd, dfStart):
    dfAll = pd.concat([dfStart[['Close']], dfEnd[['Close']]])
    df_pc = dfAll.Close.pct_change(periods=1)
    df_pc = df_pc.iloc[1:]
    df_stock = df_pc.reset_index(drop=True, inplace=False).T.rename(columns = {0:'percent'}, inplace = False)
    df_stock['percent'] = df_stock['percent'].apply(lambda x:round(x*100,2))
    df_vol = dfEnd.Volume.iloc[:1].reset_index(drop=True, inplace=False).T.rename(columns = {0: 'volume'}, inplace = False)
    df_stock['volume'] = df_vol['volume']
    return df_stock


def __getSymbolsPortPercentVol(ndays):
    start,end = md.getNDateAndToday(ndays)
    dfEnd = md.getStockPickle(end)
    endDt = md.getDescriptiveDate(dfEnd)
    dfStart = md.getStockPickle(start)
    startDt = md.getDescriptiveDate(dfStart)
    #print(startDt,endDt)
    df_stock = getStockPercentVol(dfEnd, dfStart)
    df_stock = md.getdfStockPortfolio(df_stock)
    return df_stock,endDt

def getSymbolPortPercentVol(ndays):
    df_stock,endDt = __getSymbolsPortPercentVol(ndays)
#    if account != 'Seeking Alpha':
#        df_stock = filterdfbyAccountSymbolsIdx(df_stock,account)
    return df_stock,endDt

def filterdfbyAccountSymbolsOld(dfall,account):
    if account == 'Fidelity':
        symbols = md.getFidelitySymbols()
    elif account == 'M1':
        symbols = md.getM1FinanceSymbols()
    elif account == 'Folio':
        symbols = md.getFolioInvestingSymbols()
    elif account == 'Schwab':
        symbols = md.getSchwabSymbols()
    return dfall[dfall.symbol.isin(symbols)]

def filterdfbyAccountSymbols(dfall,account):
    if account == 'Fidelity':
        symbols = md.getFidelitySymbols()
    else:
        portfolios,symbols = md.getTradingPortfoliosSymbols(account)
    return  dfall(dfall.symbol.isin(symbols))

def filterdfbyAccountSymbolsIdx(df, account):
    if account == 'Fidelity':
        symbols = md.getFidelitySymbols()
    elif account == 'M1':
        symbols = md.getM1FinanceSymbols()
    elif account == 'Folio':
        symbols = md.getFolioInvestingSymbols()
    elif account == 'Schwab':
        symbols = md.getSchwabSymbols()
    return df[df.index.isin(symbols)]
