from datetime import datetime
import pandas as pd
import market_data as md
import rh


earnings_col = 'market_data_earnings'

symbols = md.get_symbols(incl='ALL')
#symbols = ['HD','LOW','BEP','LU']
year,month,day = rh.getYearMonthDay()
year,month,day =('2021', '05', '01')
print(year,month,day)
current_month_dates = rh.getEarnings(symbols,year,month)
current_month_dates = filter(lambda x:x[1][8:10] >= day,current_month_dates)
df = pd.DataFrame(current_month_dates,columns=['symbol','earnings_date'])
df.drop_duplicates(inplace=True)

# delete current mdb records and insert new
result = earnings_col.delete_many({})
print(result.deleted_count, " documents deleted.")
try:
    result = md.add_df_to_db(df, earnings_col, dropidx=True)
    print(len(result.inserted_ids),' documents inserted')
except Exception as e:
    print('error ',e)
