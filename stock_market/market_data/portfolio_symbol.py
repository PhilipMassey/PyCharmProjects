from datetime import datetime, timedelta
import calendar

import pandas as pd
import yfinance as yf
import plotly.express as px

def getPortfolio():
    path = '/Users/philipmassey/PycharmProjects/stock_market/market_data/portfolio_symbol.csv'
    df_portfolio = pd.read_csv(path).set_index('SYMBOL')
    return df_portfolio

