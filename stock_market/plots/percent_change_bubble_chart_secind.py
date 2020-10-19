from datetime import datetime, timedelta
import calendar

import pandas as pd
import yfinance as yf
import plotly.express as px

def getNDaysAgo(ndays):
    now = datetime.now()
    start = now - pd.tseries.offsets.BusinessDay(n=(ndays+1))
    end = now - pd.tseries.offsets.BusinessDay(n=ndays)
    start = '{:%Y-%m-%d}'.format(start)
    end = '{:%Y-%m-%d}'.format(end)
    return start,end

def getPricesNDaysAgo(symbols,ndays):
    start, end = getNDaysAgo(ndays)
    #print(start,end)
    return yf.download(tickers = symbols,interval = "1d",start=start,end=end,group_by = 'column',auto_adjust = True,prepost = False,threads = True)

def getPercentVolSecInd(dfToday,dfDaysAgo,df_secind):
    dfAll = pd.concat([dfDaysAgo[['Close']],dfToday[['Close']]])
    df_pc = dfAll.Close.pct_change(periods=1)
    df_pc = df_pc.iloc[1:]
    df_stock = df_pc.reset_index(drop=True, inplace=False).T.rename(columns = {0:'percent'}, inplace = False)
    df_stock['percent'] = df_stock['percent'].apply(lambda x:round(x*100,2))
    df_stock = pd.concat([df_stock,df_secind],axis=1)
    df_vol = dfToday.Volume.iloc[:1].reset_index(drop=True, inplace=False).T.rename(columns = {0:'volume'}, inplace = False)
    df_stock['volume'] = df_vol['volume']
    #df_stock
    df_stock.reset_index(inplace=True)
    df_stock = df_stock.rename(columns = {'index':'name'})
    df_stock.sort_values(by='percent', ascending=False, inplace=True)
    return df_stock

def getEndRow(symbols):
    dfEnd = yf.download(tickers = symbols,period = "1d",interval = "1d",group_by = 'column',auto_adjust = True,prepost = False,threads = True)
    dfEnd = dfEnd.tail(1)
    date = pd.to_datetime(dfEnd.index.values[0])
    date = calendar.day_name[date.weekday()]+' '+'{:%Y-%m-%d}'.format(date)
    return dfEnd,date

def getStartRow(symbols, ndays):
    dfDaysAgo = getPricesNDaysAgo(symbols,ndays)
    #dfDaysAgo.dropna(axis='columns', inplace=True)
    dfDaysAgo = dfDaysAgo.head(1)
    date = pd.to_datetime(dfDaysAgo.index.values[0])
    date = calendar.day_name[date.weekday()]+' '+'{:%Y-%m-%d}'.format(date)
    return dfDaysAgo,date

def getSymbolsSecInd(symbols):
    market_data_dir = '/Users/philipmassey/PycharmProjects/stock_market/market_data'
    df_secind = pd.read_pickle(market_data_dir+'/name_sector_industry.pkl')
    df_secind = df_secind.set_index('name')
    df_secind = df_secind.sort_index()
    df_secind
    secinds = set(df_secind.index.values)
    diff = secinds - symbols
    return df_secind.drop(diff)

symbolsA=['A','AAU','AAPL','ABBV','ACAD','ADBE','ADM','AEM','AG','AGNC','AGR','ALRM','ALXN','AMAT','AMBA','AMD','AMGN','AMKR','AMRC','AMRN','AMT','AMZN','ANDE','ANET','ANGL','ANSS','ANTM','AOD','APH','ARE','ARGX','ARKF','ARKG','ARKK','ARKQ','ARKW','AUY','AVGO','AVNW','AVRO','AY','AYX','AZN','BAM','BAND','BE','BEP','BIDU','BIIB','BIL','BIO','BIP','BIZD','BKNG','BLD','BLDP','BLNK','BMRN','BMY','BOTZ','BPY','BYDDF','AG','CCI','CDLX','CDNS','CEF','CEVA','CHI','CHY','CI','CL','CLOU','CLSK','CNC','CNDT','CODI','COF','COHN','COMM','CONE','CPB','CPSH','CRF','CRM','CRNT','CRSP','CRWD','CSCO','CSIQ','CSOD','CTXS','CYBR','DDOG','DFP','DGX','DHI','DHR','DIA','DMRC','DNNGY','DQ','DRD','DT','DUK','DXCM','EAGG','EBAY','EDV','EELV','EEM','EEMA','EEMO','EEM','EEMV','EGHT','EGO','EMB','EMQQ','EMXC','ENB','ENPH','ERIC','ESGD','ESGE','ESGU','ESML','EVER','EVT','EXEL','FAN','FB','FBHS','FBT','FCEL','FCX','FDHY','FEDU','FFC','FFIV','FHLC','FINV','FIVG','FIVN','FLC','FLDR','FN','FND','FNV','FPE','FSLR','FSLY','FTEC','GBUY','GCTAY','GDNA','GDX','GFIN','GILD','GLO','GLW','GMAN','GNRC','GOAU','GOLD','GOOGL','GPRE','GPRO','GRAF','GRWG','GUNR','GWRE','HACK','HALO','HASI','HD','HDB','HOME','HON','HQH','HQL','HSY','HUM','IBB','IBM','IBUY','IDCC']
symbolsB = ['IEF','IEMG','IIVI','ILMN','IMMU','INFN','INO','INTC','INVA','IOVA','IPGP','IPHI','IQV','ITB','IWD','IXN','JCI','JKS','JNJ','JPI','KBH','KEY','KHC','KIRK','KLAC','KMB','KO','LEN','LGND','LH','LL','LLY','LMFA','LMNX','LOW','LQD','LRCX','LTRX','LW','MAIN','MANH','MA','MDLA','MKL','MMM','MNR','PWR','MRK','MRNA','MRVL','MSFT','MTUM','MU','MX','MXL','NEE','NEP','NET','NEWR','NEWT','NG','NIE','NIO','NKLA','NLOK','NLY','NOK','NPTN','NUAN','NVDA','NVR','NVS','NXJ','NXPI','OGIG','OKTA','OR','ORA','ORCC','PAYC','PBW','PCI','PCTY','PFE','PFPT','PHM','PHYS','PI','PING','PKI','PLUG','PSLV','PTY','PZD','QCOM','QLYS','QRVO','QTWO','REGN','REX','RGEN','RGLD','RH','RNG','ROCK','ROK','ROP','RPAR','RPM','RSP','RUN','SAIL','SAND','SANM','SAP','SBAC','SBRCY','CCO','SDGR','SEDG','SGDM','SHOP','SHV','SHY','SIL','SIVR','SJM','SKYY','SLV','SLYV','SMG','SNP','SNSR','SOGO','SOLO','SPWR','SQ','SSD','SSNC','ST','STX','SUSB','SUSC','SWI','SWIR','SWK','TAN','TDF','TECH','THW','TIGR','TLT','TMO','TOL','TOT','TPIC','TSLA','TSM','TWLO','TXN','TYL','UFPI','UNH','USHY','VCLT','VCSH','VEA','VEEV','VG','VGSH','VIAV','VIGI','VNQ','VRTX','VSLR','VUG','VWDRY','WAT','WCLD','WKHS','WORK','WPM','XBI','XLNX','XPH','ZM','ZS','ZUO']
symbols=symbolsA+symbolsB
#symbols = ['AAPL','CLSK','DCT','TWTR','ODFL','TCEHY']
symbols = set(symbols)
print(len(symbols))
df_secind = getSymbolsSecInd(symbols)

dfEnd, end = getEndRow(symbols)

def plotPercentVolSecInd(symbols, ndays,title,dfEnd,df_secind):
    dfStart, start = getStartRow(symbols, ndays)
    print(start)
    print(dfStart[['Close']])
    df_stock = getPercentVolSecInd(dfEnd, dfStart, df_secind)
    if len(title) = 0:
        title = '{} - {} percent change to {}'.format('SECTORS', start, end)
    fig = px.scatter(df_stock[:40], x="sector", y="percent",
                     size="volume", color="volume", title=title,
                     hover_name="name", log_x=False, log_y=False,
                     size_max=80, width=1600, height=1000)
    fig.show()
    # title = '{} - {} percent change to {}'.format('INDUSTRY', start, end)
    # fig = px.scatter(df_stock[:40], x="industry", y="percent",
    #                  size="volume", color="volume", title=title,
    #                  hover_name="name", log_x=False, log_y=False,
    #                  size_max=80, width=1600, height=1000)
    # fig.show()
ndays = 0
plotPercentVolSecInd(symbols,ndays,title='',dfEnd=dfEnd,df_secind=df_secind)
ndays = 3
plotPercentVolSecInd(symbols,ndays,title='',dfEnd,df_secind)
ndays = 10
title = '{} - {} days percent change'.format('SECTORS',ndays)
plotPercentVolSecInd(symbols,ndays,title=title,dfEnd,df_secind)
ndays = 60
title = '{} - {} days percent change'.format('SECTORS',ndays)
plotPercentVolSecInd(symbols,ndays,dfEnd,df_secind)
