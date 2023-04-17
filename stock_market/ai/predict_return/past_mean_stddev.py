import pandas as pd
import numpy as np

# Load the data from a CSV file
data = pd.read_csv('stock_prices.csv')

# Calculate the percentage change in price for each stock over the last year
returns = data.pct_change(10)

# Calculate the mean and standard deviation of the percentage change for each stock
mean_returns = returns.mean()
std_returns = returns.std()

# Calculate the mean percentage increase in price over the last year for each stock
mean_increase = (1 + mean_returns) ** 1 - 1

# Find the stock with the highest mean increase and the lowest standard deviation
best_stock = mean_increase[std_returns == std_returns.min()].idxmax()

print('The stock with the highest mean percentage increase and the lowest standard deviation is:', best_stock)
