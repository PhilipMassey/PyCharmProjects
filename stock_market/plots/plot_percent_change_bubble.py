import portfolio as pf
import plotly.express as px

def plotPercentVolPortfolio(df_stock,ndays,endDt):
    df_stock.reset_index(inplace=True)
    df_stock = df_stock.rename(columns={'index': 'name'})
    df_stock.sort_values(by='percent', ascending=False, inplace=True)
    df_stock=df_stock[:40]
    df_stock.sort_values(by='portfolio',inplace=True)
    title = '{} - {}  {} days percent change'.format('PORTFOLIOS', endDt,ndays)

    fig = px.scatter(df_stock[:40], x="portfolio", y="percent",
                     size="volume", color="volume", title=title,
                     hover_name="name", log_x=False, log_y=False,
                     size_max=80, width=1600, height=1000)
    fig.show()