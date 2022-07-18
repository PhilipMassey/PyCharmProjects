import market_data as md

import pandas as pd
import apis

import plotly.graph_objects as go


def main():
    # Get the data
    df = md.get_data()

    # Get the data from the API
    api_df = apis.get_data()

    # Merge the dataframes
    df = df.merge(api_df, on='date', how='outer')
    go.bar(df)
    df.to_csv('data/test/github_buddy.csv')
