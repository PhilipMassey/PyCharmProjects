import market_data as md
import pandas as pd

def getStockPercentVolOLD(dfEnd, dfStart):
    dfAll = pd.concat([dfStart[['Close']], dfEnd[['Close']]])
    df_pc = dfAll.Close.pct_change(periods=1)
    df_pc = df_pc.iloc[1:]
    df_stock = df_pc.reset_index(drop=True, inplace=False).T.rename(columns = {0:'percent'}, inplace = False)
    df_stock['percent'] = df_stock['percent'].apply(lambda x:round(x*100,2))
    df_vol = dfEnd.Volume.iloc[:1].reset_index(drop=True, inplace=False).T.rename(columns = {0: 'volume'}, inplace = False)
    df_stock['volume'] = df_vol['volume']
    return df_stock


def __getSymbolsPortPercentVolOld(ndays):
    start,end = md.getNDateAndToday(ndays)
    dfEnd = md.getStockPickle(end)
    endDt = md.getDescriptiveDate(dfEnd)
    dfStart = md.getStockPickle(start)
    startDt = md.getDescriptiveDate(dfStart)
    #print(startDt,endDt)
    df_stock = getStockPercentVol(dfEnd, dfStart)
    df_stock = md.addPortfolioTodf_stock(df_stock)
    return df_stock,endDt

def __getSymbolsPortPercentVol(ndays):
    start,end = md.getNDateAndToday(ndays)
    dfEnd = md.getStockPickle(end)
    endDt = md.getDescriptiveDate(dfEnd)
    dfStart = md.getStockPickle(start)
    startDt = md.getDescriptiveDate(dfStart)
    #print(startDt,endDt)
    df_stock = getStockPercentVol(dfEnd, dfStart)
    df_stock = md.addPortfolioTodf_stock(df_stock)
    return df_stock,endDt

def getStockPercent(dfCloseStart, dfCloseEnd):
    dfCloseStart.dropna(inplace=True,how='all');dfCloseEnd.dropna(inplace=True,how='all')
    dfAll = pd.concat([dfCloseStart, dfCloseEnd])
    df_pc = dfAll.pct_change(periods=1)
    df_pc = df_pc.iloc[1:]
    df_stock = df_pc.reset_index(drop=True, inplace=False).T.rename(columns = {0:'percent'}, inplace = False)
    df_stock['percent'] = df_stock['percent'].apply(lambda x:round(x*100,2))
    return df_stock

def getStockVol(dfVolEnd):
    df_vol = dfVolEnd.iloc[:1].reset_index(drop=True, inplace=False).T.rename(columns = {0: 'volume'}, inplace = False)
    return df_vol['volume']

def getSymbolPortPercentVol(start,end):
    dfCloseStart, dfVolStart = md.getMdbRowsCloseVol(start)
    dfCloseEnd, dfVolEnd = md.getMdbRowsCloseVol(end)
    df_stock = getStockPercent(dfCloseStart,dfCloseEnd)
    df_stock['volume'] = getStockVol(dfVolEnd)
    df_stock = md.addPortfolioTodf_stock(df_stock)
    endDt = md.getDescriptiveDate(dfCloseEnd)
    return df_stock, endDt

def filterdfbyAccountSymbols(dfall,account):
    if account == 'fidelity':
        symbols = md.getFidelitySymbols()
    else:
        portfolios,symbols = md.getTradingPortfoliosSymbols(account)
    return  dfall[dfall.symbol.isin(symbols)]

def filterdfbyAccountSymbolsIdx(df, account):
    if account == 'fidelity':
        symbols = md.getFidelitySymbols()
    elif account == 'm1':
        symbols = md.getM1FinanceSymbols()
    elif account == 'folio':
        symbols = md.getFolioInvestingSymbols()
    elif account == 'schwab':
        symbols = md.getSchwabSymbols()
    return df[df.index.isin(symbols)]
