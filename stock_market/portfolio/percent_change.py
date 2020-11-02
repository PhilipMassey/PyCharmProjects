import market_data as md
import pandas as pd

def getPercentVol(dfEnd, dfStart):
    dfAll = pd.concat([dfStart[['Close']], dfEnd[['Close']]])
    df_pc = dfAll.Close.pct_change(periods=1)
    df_pc = df_pc.iloc[1:]
    df_stock = df_pc.reset_index(drop=True, inplace=False).T.rename(columns = {0:'percent'}, inplace = False)
    df_stock['percent'] = df_stock['percent'].apply(lambda x:round(x*100,2))
    df_vol = dfEnd.Volume.iloc[:1].reset_index(drop=True, inplace=False).T.rename(columns = {0: 'volume'}, inplace = False)
    df_stock['volume'] = df_vol['volume']
    return df_stock

def getdfStockPortfolio(df_stock):
    df_port = md.getPortfolios()
    df_stock = pd.concat([df_stock,df_port],axis=1)
    return df_stock

def getPercentVolPort(days):
    ndays = 0
    dfEnd = md.getNDaysStockPickle(ndays)
    endDt = md.getDescriptiveDate(dfEnd)
    ndays = days
    dfStart = md.getNDaysStockPickle(ndays)
    startDt = md.getDescriptiveDate(dfStart)
    print(startDt,endDt)
    df_stock = getPercentVol(dfEnd,dfStart)
    df_stock = getdfStockPortfolio(df_stock)
    return df_stock,endDt

