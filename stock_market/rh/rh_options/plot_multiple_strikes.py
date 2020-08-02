import warnings
warnings.filterwarnings("ignore")

import robin_stocks as r
import pandas as pd
import plotly.express as px
from operator import itemgetter, attrgetter, methodcaller

from rh.rh_options import diffMaxHighLow
from rh.main import utcToLocal

def getStrikePrices(symbol,expirationDate,optionType='call',volume_limit=0):
    #options = r.find_options_for_list_of_stocks_by_expiration_date([symbol], expirationDate=expirationDate,optionType=optionType)
    options = r.find_options_by_expiration([symbol], expirationDate=expirationDate,optionType=optionType)
    dfoptions = pd.DataFrame((filter(lambda x:x['volume']>volume_limit,options)))
    if dfoptions.empty:
        print('Volume is 0 for options')
    else:
        #dfoptions[['strike_price','high_price','low_price']] = dfoptions[['strike_price','high_price','low_price']].apply(pd.to_numeric)
        #dfstrike_prices = dfoptions.sort_values(by='volume',ascending=False)[0:5][['strike_price','volume']]
        #dfstrike_prices.sort_values(by='strike_price',inplace=True)
        dfstrike_prices = dfoptions.sort_values(by='volume',ascending=False)[0:5][['strike_price','volume']].apply(pd.to_numeric)
        dfstrike_prices.sort_values(by='strike_price',ascending=True,inplace=True)
    return dfstrike_prices


def plotPricesForExpriation(ohlc, symbol, expirationDate, dfstrike_prices, span='week', optionType='call', ):
    """
    :param OHLC: open_price, high_price, low_price, close_price
    :param symbol:
    :param expirationDate:
    :param dfstrike_prices:
    :param optionType:
    :param span:
    :return:
    """
    df_all = pd.DataFrame()
    for idx, row in dfstrike_prices.iterrows():
        strike_price = row.strike_price
        # print('Strike price: {}'.format(strike_price))
        df = pd.DataFrame(
            r.get_option_historicals(symbol, expirationDate, strike_price, optionType, span))
        if df.empty:
            print('No options\t{}\t{}\t{}'.format(expirationDate,strike_price,span))
            return
        df['strike_price'] = strike_price
        df[['strike_price','open_price','high_price','low_price','close_price']] = df[['strike_price','open_price','high_price','low_price','close_price']].apply(pd.to_numeric)
        ohlc_price = df[ohlc].iloc[0]
        df['diff'] = df[ohlc] - ohlc_price
        df['pct_change'] = 0 if ohlc_price == 0 else round(df['diff'] / ohlc_price, 2)
        df_all = pd.concat([df_all,df[['begins_at','strike_price','close_price','high_price','pct_change','low_price','open_price','volume']]])
    # df_all = df_all[df_all != 0.01]
    df_all = df_all[df.high_price != df.high_price[0:1][0]]  # filter no changes form the starting date

    print()
    diffMaxHighLow(df_all, dfstrike_prices)
    local = utcToLocal(df_all.iloc[-1:].begins_at.values[-1])
    title = 'Percent change {} Expiration:{}, Time:{:{dfmt} {tfmt}}'.format(symbol, expirationDate, local, dfmt='%Y-%m-%d',
                                                             tfmt='%H:%M')
    fig = px.line(df_all, x="begins_at", y="pct_change", color="strike_price", line_group="strike_price",
                  hover_name="strike_price",
                  line_shape="spline", render_mode="svg")
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Pct Change",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        ))
    fig.show()

    title = 'Close Price {} Expiration:{}, Time:{:{dfmt} {tfmt}}'.format(symbol, expirationDate, local, dfmt='%Y-%m-%d',
                                                             tfmt='%H:%M')
    fig = px.line(df_all, x="begins_at", y="close_price", color="strike_price", line_group="strike_price",
                  hover_name="strike_price",
                  line_shape="spline", render_mode="svg")
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Close Price",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        ))
    fig.show()