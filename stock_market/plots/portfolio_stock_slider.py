import portfolio as pf
import market_data as md
import pandas as pd
import plotly.express as px

def plotPortPercPeriods(dfa,title,barorbubble):
    print('{} {}'.format(min(dfa.percent.values),max(dfa.percent.values)))
    dfa.sort_values(by=['date','portfolio'], ascending=[False,True],inplace=True)
    if barorbubble == 'bubble':
        fig = px.scatter(dfa, x="portfolio", y="percent",
                         animation_frame="date", animation_group="date",
                        size="volume", color="portfolio", hover_name="portfolio",
                        llog_x=False, log_y=False,
                         size_max=55,
                        range_x=[0,len(set(dfa.portfolio.values))],
                        range_y=[min(dfa.percent.values),max(dfa.percent.values)],
                        width=1450, height=1000,
                        title=title)
    else:
        fig = px.bar(dfa, x="portfolio", y="percent",
                     color="portfolio", hover_name="portfolio",
                     animation_frame="date", animation_group="date",
                     log_x=False, log_y=False,
                     range_x=[0,len(set(dfa.portfolio.values))],
                     range_y=[min(dfa.percent.values),max(dfa.percent.values)],
                     width=1450, height=1000,
                     title=title)

    fig["layout"].pop("updatemenus")  # optional, drop animation buttons
    fig.show()


def plotSymPercPerdiod(dfa,title,barorbubble):
    dfa.sort_values(by=['date','portfolio'], ascending=[False,True],inplace=True)
    if barorbubble == 'bar':
        fig = px.bar(dfa, x="portfolio", y="percent",
                        color="symbol", hover_name="portfolio",
                        animation_frame="date", animation_group="date",
                        log_x=False, log_y=False,
                        range_x=[0,len(set(dfa.portfolio.values))], range_y=[min(dfa.percent.values),max(dfa.percent.values)],
                        width=1450, height=1000,title=title)
    elif barorbubble == 'bubble':
        dfa = dfa[dfa.volume.values >0]
        fig = px.scatter(dfa, x="portfolio", y="percent",
                         size="volume", color="symbol", hover_name="portfolio",
                         log_x=False, log_y=False,
                         size_max=55,
                        animation_frame="date", animation_group="date",
                        range_x=[0,len(set(dfa.portfolio.values))], range_y=[min(dfa.percent.values),max(dfa.percent.values)],
                        width=1450, height=1000,title=title)
    elif barorbubble == 'barsymbol':
        dfa = dfa[dfa.volume.values > 0]
        fig = px.bar(dfa, x="symbol", y="percent",
                     color="symbol", hover_name="symbol",
                     log_x=False, log_y=False,
                     animation_frame="date", animation_group="date",
                     range_x=[0, len(set(dfa.symbol.values))],
                     range_y=[min(dfa.percent.values), max(dfa.percent.values)],
                     width=1450, height=1000, title=title)

    fig["layout"].pop("updatemenus") # optional, drop animation buttons

    fig.show()

def plotPercentVolPortfolio(dfa,title,barorbubble):
    dfa.sort_values(by='percent', ascending=ascending, inplace=True)
    title =title

    fig = px.scatter(dfa, x="portfolio", y="percent",
                     size="volume", color="volume", title=title,
                     log_x=False, log_y=True,
                     hover_name="name",
                     size_max=80, width=1600, height=1000)
    fig.show()