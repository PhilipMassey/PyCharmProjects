import pandas as pd
from pymongo import MongoClient
client = MongoClient()
db = client[md.db_client]
collection = db[md.db_close]

# Define the stocks and date range to extract
stocks = ['AAPL', 'GOOG']
start_date = '2022-01-01'
end_date = '2022-03-31'

# Query the MongoDB database for the selected stocks and date range
query = {'symbol': {'$in': stocks}, 'Date.$date': {'$gte': start_date, '$lte': end_date}}
projection = {'symbol': 1, 'Date.$date': 1, 'close': 1}
data = list(collection.find(query, projection))

# Convert the MongoDB data to a pandas DataFrame
data_df = pd.DataFrame(data)
data_df = data_df.rename(columns={'Date.$date': 'date', 'symbol': 'stock', 'close': 'price'})
data_df = data_df.set_index(['date', 'stock'])
data_df = data_df.unstack()
data_df.columns = data_df.columns.get_level_values(1)

# Calculate the returns over the previous 1, 2, and 3 months
returns_df = data_df.pct_change()
returns_df = returns_df.dropna()
returns_df_1m = returns_df[-20:]
returns_df_2m = returns_df[-40:-20]
returns_df_3m = returns_df[:-40]

# Create a binary indicator variable for positive returns over the next month
positive_return = returns_df_1m.apply(lambda x: x > 0).astype(int)

# Merge the returns and positive_return DataFrames and save to CSV
stocks_data = pd.concat([returns_df_1m, returns_df_2m, returns_df_3m, positive_return], axis=1)
stocks_data.to_csv('stocks_data.csv')
