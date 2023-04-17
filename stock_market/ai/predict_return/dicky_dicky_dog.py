##
# Here's an example Python program using scikit-learn to predict the highest percentage gain
# for the lowest standard deviation in the weekly price change over the next 3 months:

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Each row in the file represents a particular date,
# and each column represents the closing price of a particular stock
data = pd.read_csv('stocks_data.csv')

# Compute the weekly price changes
weekly_changes = data.pct_change(periods=5)

# Compute the standard deviation of the weekly changes
std_devs = StandardScaler().fit_transform(weekly_changes.dropna().values)

# Create a new DataFrame for the predictions
predictions = pd.DataFrame()

# Create a pipeline for each stock
for col in weekly_changes.columns:
    # Drop NaN values and get the target variable (weekly change over the next 3 months)
    target = weekly_changes[col].pct_change(periods=-13).dropna().values

    # Create a pipeline with a linear regression model
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LinearRegression())
    ])

    # Fit the pipeline to the data and make a prediction for the next 3 months
    pipeline.fit(weekly_changes.dropna().values, target)
    next_3_months = pipeline.predict(weekly_changes.tail(65).values.reshape(1, -1))[0]

    # Compute the mean and standard deviation of the target variable
    target_mean = np.mean(target)
    target_std = np.std(target)

    # Compute the ratio of the mean to the standard deviation
    if target_std != 0:
        ratio = target_mean / target_std
    else:
        ratio = 0

    # Add the prediction and the ratio to the DataFrame
    predictions[col] = [next_3_months, ratio]

# Find the stock with the highest ratio
best_stock = predictions.loc['ratio'].idxmax()

# Print the result
print(
    f"The stock with the highest percentage gain for the lowest standard deviation in the next 3 months is {best_stock}, with a ratio of {predictions.loc['ratio', best_stock]:.2f}.")
