import market_data as md
import pandas as pd

def getStockPercent(dfCloseStart, dfCloseEnd):
    dfCloseStart.dropna(inplace=True,how='all');dfCloseEnd.dropna(inplace=True,how='all')
    dfAll = pd.concat([dfCloseStart, dfCloseEnd])
    df_pc = dfAll.pct_change(periods=1)
    df_pc = df_pc.iloc[1:]
    df_stock = df_pc.reset_index(drop=True, inplace=False).T.rename(columns = {0:'percent'}, inplace = False)
    df_stock['percent'] = df_stock['percent'].apply(lambda x:round(x*100,2))
    return df_stock

def getStockVol(dfVol):
    df_vol = dfVol.iloc[:1].reset_index(drop=True, inplace=False).T.rename(columns = {0: 'volume'}, inplace = False)
    return df_vol['volume']

def getSymbolPortPercentVol(start,end,incl):
    dfCloseStart, dfVolStart = md.getMdbRowsCloseVol(start,incl)
    dfCloseEnd, dfVolEnd = md.getMdbRowsCloseVol(end,incl)
    df_stock = getStockPercent(dfCloseStart,dfCloseEnd)
    df_stock['volume'] = getStockVol(dfVolEnd)
    df_stock = md.addPortfolioTodf_stock(df_stock,incl)
    endDt = md.getDescriptiveDate(dfCloseEnd)
    return df_stock, endDt

