import pandas as pd
path ='/Users/philipmassey/PycharmProjects/stock_market/market_data/portfolio_symbol.csv'

df_portfolio = pd.read_csv(path)
print(df_portfolio.head(5))

symbolsA=['A','AAU','AAPL','ABBV','ACAD','ADBE','ADM','AEM','AG','AGNC','AGR','ALRM','ALXN','AMAT','AMBA','AMD','AMGN','AMKR','AMRC','AMRN','AMT','AMZN','ANDE','ANET','ANGL','ANSS','ANTM','AOD','APH','ARE','ARGX','ARKF','ARKG','ARKK','ARKQ','ARKW','AUY','AVGO','AVNW','AVRO','AY','AYX','AZN','BAM','BAND','BE','BEP','BIDU','BIIB','BIL','BIO','BIP','BIZD','BKNG','BLD','BLDP','BLNK','BMRN','BMY','BOTZ','BPY','BYDDF','AG','CCI','CDLX','CDNS','CEF','CEVA','CHI','CHY','CI','CL','CLOU','CLSK','CNC','CNDT','CODI','COF','COHN','COMM','CONE','CPB','CPSH','CRF','CRM','CRNT','CRSP','CRWD','CSCO','CSIQ','CSOD','CTXS','CYBR','DDOG','DFP','DGX','DHI','DHR','DIA','DMRC','DNNGY','DQ','DRD','DT','DUK','DXCM','EAGG','EBAY','EDV','EELV','EEM','EEMA','EEMO','EEM','EEMV','EGHT','EGO','EMB','EMQQ','EMXC','ENB','ENPH','ERIC','ESGD','ESGE','ESGU','ESML','EVER','EVT','EXEL','FAN','FB','FBHS','FBT','FCEL','FCX','FDHY','FEDU','FFC','FFIV','FHLC','FINV','FIVG','FIVN','FLC','FLDR','FN','FND','FNV','FPE','FSLR','FSLY','FTEC','GBUY','GCTAY','GDNA','GDX','GFIN','GILD','GLO','GLW','GMAN','GNRC','GOAU','GOLD','GOOGL','GPRE','GPRO','GRAF','GRWG','GUNR','GWRE','HACK','HALO','HASI','HD','HDB','HOME','HON','HQH','HQL','HSY','HUM','IBB','IBM','IBUY','IDCC']
symbolsB = ['IEF','IEMG','IIVI','ILMN','IMMU','INFN','INO','INTC','INVA','IOVA','IPGP','IPHI','IQV','ITB','IWD','IXN','JCI','JKS','JNJ','JPI','KBH','KEY','KHC','KIRK','KLAC','KMB','KO','LEN','LGND','LH','LL','LLY','LMFA','LMNX','LOW','LQD','LRCX','LTRX','LW','MAIN','MANH','MA','MDLA','MKL','MMM','MNR','PWR','MRK','MRNA','MRVL','MSFT','MTUM','MU','MX','MXL','NEE','NEP','NET','NEWR','NEWT','NG','NIE','NIO','NKLA','NLOK','NLY','NOK','NPTN','NUAN','NVDA','NVR','NVS','NXJ','NXPI','OGIG','OKTA','OR','ORA','ORCC','PAYC','PBW','PCI','PCTY','PFE','PFPT','PHM','PHYS','PI','PING','PKI','PLUG','PSLV','PTY','PZD','QCOM','QLYS','QRVO','QTWO','REGN','REX','RGEN','RGLD','RH','RNG','ROCK','ROK','ROP','RPAR','RPM','RSP','RUN','SAIL','SAND','SANM','SAP','SBAC','SBRCY','CCO','SDGR','SEDG','SGDM','SHOP','SHV','SHY','SIL','SIVR','SJM','SKYY','SLV','SLYV','SMG','SNP','SNSR','SOGO','SOLO','SPWR','SQ','SSD','SSNC','ST','STX','SUSB','SUSC','SWI','SWIR','SWK','TAN','TDF','TECH','THW','TIGR','TLT','TMO','TOL','TOT','TPIC','TSLA','TSM','TWLO','TXN','TYL','UFPI','UNH','USHY','VCLT','VCSH','VEA','VEEV','VG','VGSH','VIAV','VIGI','VNQ','VRTX','VSLR','VUG','VWDRY','WAT','WCLD','WKHS','WORK','WPM','XBI','XLNX','XPH','ZM','ZS','ZUO']
symbolsC = ['DCT','GRAF','TWTR','ODFL','TCEHY']
symbols=set(symbolsA+symbolsB+symbolsC)

df_symbols = pd.DataFrame(data=symbols,columns=['SYMBOLS'])
print(df_symbols.head(5))

df_symbols.set_index(keys='SYMBOL')['PORTFOLIO'] = df_portfolio.set_index(keys='SYMBOL')['PORTFOLIO']
