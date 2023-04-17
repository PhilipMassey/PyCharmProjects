import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the data
# CSV file called "stocks_data.csv", with the following columns:
# "stock": the name of the stock
# "1_month_return": the return of the stock over the past month
# "2_month_return": the return of the stock over the past 2 months
# "3_month_return": the return of the stock over the past 3 months
# "positive_return": a binary indicator variable that is 1 if the stock had a positive return over the next month, and 0 otherwise

data = pd.read_csv("stocks_data.csv")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop("positive_return", axis=1), data["positive_return"], test_size=0.2, random_state=42)

# Train the logistic regression model
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Predict the probability of a positive return for the test set
probabilities = lr.predict_proba(X_test)[:,1]

# Print the probabilities for each stock
for i in range(len(X_test)):
    print("Stock:", X_test.iloc[i]["stock"])
    print("1-month probability:", probabilities[i])
    print("2-month probability:", lr.predict_proba([X_test.iloc[i]["1_month_return"]])[0][1])
    print("3-month probability:", lr.predict_proba([X_test.iloc[i]["3_month_return"]])[0][1])
