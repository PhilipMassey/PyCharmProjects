import market_data as md


def get_mdb_steady(ndays,db_colln):
    df = md.get_mdb_row_for_nday(ndays, db_colln)
    return df.symbol.values
