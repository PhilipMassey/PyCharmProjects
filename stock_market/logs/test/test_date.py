import market_data as md


ndays_period = md.get_ndays_range_montlhly()
print('get_ndays_range_montlhly: ', ndays_period)
ndays_range = md.get_ndays_range_wfm3612()
print('get_ndays_range_wfm3612: ', ndays_range)

print(md.get_date_for_mdb(60))
print(md.get_nbusdays_from_datestr('2021-09-10'))