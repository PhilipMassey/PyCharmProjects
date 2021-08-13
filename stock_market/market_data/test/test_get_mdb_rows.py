import market_data as md
from pymongo import MongoClient


client = MongoClient()
db = client[md.db_client]
start = 0
end = 5

#[md.get_mdb_row_for_nday(ndays,md.db_close) for ndays in range(start, end)]
symbols = md.get_symbols(incl=md.all)
[md.get_missing_market_row(ndays,symbols) for ndays in range(start, end)]
