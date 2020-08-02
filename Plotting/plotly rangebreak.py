import plotly.express as px
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.scatter(df, x='Date', y='AAPL.High', range_x=['2015-12-01', '2016-01-15'],
                 title="Hide Gaps with rangebreaks")
fig.update_xaxes(
    range=[
        dict(bounds=["sat", "mon"]), #hide weekends
        dict(values=["2015-12-25", "2016-01-01"])  # hide Christmas and New Year's
    ]
)
fig.show()