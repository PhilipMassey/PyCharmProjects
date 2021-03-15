import market_data as md

# Check unigue symbols
def checkSymbolsUnique():
    df_port = md.getPortfoliosAndSymbols()
    usymbols = list(df_port.symbol.unique())
    usymbols.sort()
    symbols = list(df_port.symbol.values)
    symbols.sort()
    x = [j for i, j in zip(usymbols, symbols) if i != j]
    if len(x)>0:
        print(x[0])
    else:
        print('no dups')


checkSymbolsUnique()
