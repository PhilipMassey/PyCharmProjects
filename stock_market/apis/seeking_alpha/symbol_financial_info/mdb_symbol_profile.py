import market_data as md
profile_fields_short ['Date', 'symbol', 'peRatioFwd', 'estimateEps', 'divYield', 'shortIntPctFloat', 'marketCap','volume']
profile_fields_long = ['Date','divYield','eps','estimateEps','evEbit','evEbitda','evFcf','evSales','fcf','fcfShare',
'ltDebtCap','marketCap','movAvg10d','movAvg10w','movAvg200d','payout4y','payoutRatio','pegRatio','peRatioFwd','priceBook','priceCf','priceSales','priceTangb','quickRatio','revenueGrowth','revenueGrowth3','roa','roe','shares','shortIntPctFloat','symbol','volume']

def df_mdb_symbol_profile(symbol):
    db_coll_name = md.db_symbol_profile
    ndays = 0
    period = 1000
    symbols = [symbol]
    df = md.df_mdb_between_days(ndays, period, symbols, db_coll_name, fields)
    df.index = df.index.strftime('%m/%d/%Y')
    df = df.T
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'Date'})
    return df

def df_mdb_symbol_info(symbol):
    db_coll_name = md.db_symbol_info
    ndays = 0
    period = 1000
    symbols = [symbol]
    #fields = ['Date', 'symbol', 'peRatioFwd', 'estimateEps', 'divYield', 'shortIntPctFloat', 'marketCap','volume']
    #fields = ['Date','divYield','eps','estimateEps','evEbit','evEbitda','evFcf','evSales','fcf','fcfShare',
'ltDebtCap','marketCap','movAvg10d','movAvg10w','movAvg200d','payout4y','payoutRatio','pegRatio','peRatioFwd','priceBook','priceCf','priceSales','priceTangb','quickRatio','revenueGrowth','revenueGrowth3','roa','roe','shares','shortIntPctFloat','symbol','volume']
    df = md.df_mdb_between_days(ndays, period, symbols, db_coll_name, fields)
    df.index = df.index.strftime('%m/%d/%Y')
    df = df.T
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'Date'})
    return df
