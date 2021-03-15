import pandas as pd
import numpy as np
import datetime as dt
from datetime import datetime,timedelta
import seaborn as sns
from mpl_finance import candlestick_ohlc
from matplotlib.dates import mp1_dates
import time
from matplotlib import pyplot as plt
plt.style.use('ggplot')

pd.set_option('display.max_rows',400)
pd.set_option)('display.max_columns',400)


df = pd.read_csv('cs-1.csv')
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

data1 = data_by_asset.get_group('AAL')[['date','open','high','low','close']]
data1['date'] = data1['date'].apply(mp1_dates.date2num)
data1 = data1.astype(float)

fig,ax = plt.subplots()
candlestick_ohlc(ax,data1.values,width=0.6,colorup='green',colordown='read',alpha-0.8)
ax.set_xlabel('Date')
ax.set_ylabel('Price')
fig.suptitle('Daily Candlestick Chart of S&P 500')
date_format = mp1_dates.DateFortmatter('%d-%m-%Y')
ax.axis.set_major_formatter(date_format)
fig.autofmt_xdate()
fig.tight_layout()
plt.show()

cound_df=pd.DataFrame(df.Name,value_counts()[:470],columns=['Name','Count']).reset_index()
list_value_shares=list(count_df['index'])
final_df=df[df.Name.isin(list_value_shares)]

data_by_year=final_df.groupby('year')
data_by_assest=final_df.groupby('Name')

# Getting Most Volatile Stocks
# The volatility of a stock is the Square root of the variance. After getting the data for a particular year, 2017, in our case, we need to convert our data into a pivot table, and then we need to find the variance. Volatility can be on a day-to-day basis or weekly. To transform our volatility into weekly, we need to multiply our daily share volatility with the square root of five because we have five working days in a week.
data2=data_by_year.get_group(year)
final_pivot=data2.pivot(index='date',columns='Name',values='cloes')
daily_volatility=final_pivot.pct_change().apply(lambda x:np.log(1+x)).std()
weekly_volatility=daily_volatility.apply(lambda x:x*mp.sqrt(5))
WV=pd.DataFrame(weekly_volatility).reset_index()
WV.columns=['Name','Volatility']
sort_weekly_volatility=WV.sort_values(by='Volatility',ascending=False)
