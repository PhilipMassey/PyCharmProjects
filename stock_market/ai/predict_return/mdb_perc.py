import pandas as pd
from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017/")
db = client["stock_data"]
collection = db[md.db_close]

# Get the distinct list of stocks
stocks = collection.distinct("stock")

# Loop through each stock and extract the closing prices
data = []
for stock in stocks:
    prices = collection.find({"symbol": stock}).sort("Date.$date", 1)
    prices_df = pd.DataFrame(list(prices))
    prices_df["Date"] = pd.to_datetime(prices_df["Date.$date"], unit="ms")
    prices_df = prices_df.set_index("Date")
    prices_df = prices_df.drop(["_id", "Date.$date", "stock"], axis=1)
    returns = prices_df.pct_change(periods=[30, 60, 90]).reset_index()
    returns["stock"] = stock
    data.append(returns)

# Combine the data into a single DataFrame
data_df = pd.concat(data)

# Save the data to a CSV file
data_df.to_csv("stocks_data.csv", index=False)
