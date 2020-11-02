import portfolio as pf

df_port = pf.getPortfolios()
symbols = list(df_port.index.values)
def getSymbolPortfolio(symbol):
    mylist = [symbols]
    return df_port[df_port.index.isin(mylist)]

# Check unigue symbols
df checkSymbolsUnique():
    ndays=0
    df_stock = pf.getdfDaysAgo(symbols,ndays)
    df_stock = df_stock[['Close']]
    print(df_stock.size)
    print(df_port.size)
    l_stock = list(df_stock['Close'].values)
    l_stock.sort()
    l_port = list(df_port.index.values)
    l_port.sort()
    [j for i,j in zip(l_stock,l_port) if i != j]

