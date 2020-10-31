import portfolio as pf
import plotly.express as px

def plotPercentVolPortfolio(symbols, ndays, title, dfEnd, endDt, df_port):
    dfStart, startDt = pf.getRowNDaysAgo(symbols, ndays)
    df_stock = pf.getPercentVolPortfolio(dfEnd, dfStart, df_port)
    df_stock.sort_values(by='percent', ascending=False, inplace=True)
    df_stock=df_stock[:40]
    df_stock.sort_values(by='portfolio',inplace=True)
    if len(title) == 0:
        title = '{} - {} percent change to {}'.format('PORTFOLIOS', startDt, endDt)
    fig = px.scatter(df_stock[:40], x="portfolio", y="percent",
                     size="volume", color="volume", title=title,
                     hover_name="name", log_x=False, log_y=False,
                     size_max=80, width=1600, height=1000)
    fig.show()