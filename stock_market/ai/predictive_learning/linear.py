#https://medium.com/@dniggl/stock-market-prediction-using-machine-learning-dd064a7561f1
import pandas as pd
import yfinance as yf
import datetime
import numpy as np
import matplotlib.pyplot as plt
ticker = 'TROX'
stock_df = yf.download(ticker, start='2020-01-10', end='2021-01-10', progress=False)[['Close']]
stock_df = pd.concat([stock_df, stock_df.shift(), stock_df.shift(2), stock_df.shift(3), stock_df.shift(4), stock_df.shift(5),
                      stock_df.shift(6), stock_df.shift(7), stock_df.shift(8), stock_df.shift(9), stock_df.shift(10)], axis=1).dropna()
stock_df.columns = list(range(0, 11))
stock_df.rename(columns={0: 'actual_stock_price'}, inplace=True)
stock_df.head()
# Split the data into training and test data sets.
train = stock_df.head(len(stock_df) - 10)
test = stock_df.tail(10)

# Import the Lineear Regression model from scikit-learn.
from sklearn.linear_model import LinearRegression
# Create the model object.
LR = LinearRegression()

# Train the model on the training data.
LR.fit(train[list(range(1,11))],train['actual_stock_price'])

# Make predictions on the test data.
test['predictions'] = LR.predict(test[list(range(1,11))])
# Visualize the actual stock price and the predicted stock price    # over the time period.
plt.figure(figsize=(12,7))
ax = test[['actual_stock_price','predictions']].plot(figsize=(12,8))
plt.xlabel('Date', fontsize=12)
plt.ylabel('Stock Price', fontsize=12)
plt.title('Actual and Predicted Stock Prices', fontsize=15)
plt.grid()
plt.show()