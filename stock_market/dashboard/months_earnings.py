import dash
import dash_html_components as html
import dash_core_components as dcc
import market_data as md
from pymongo import MongoClient
import numpy as np

def getCurrentMonthEarnings():
    client = MongoClient()
    db = client['stock_market']
    earnings_col = db['market_data_earnings']
    mongo_data= earnings_col.find({})
    df = md.MdbToDataframe(mongo_data)
    df.drop(['_id.$oid'], axis=1, inplace=True)
    return np.sort(list(df.to_records(index=False)), order=['earnings_date', 'symbol'])


app = dash.Dash(__name__)
app.title='Earnings'
alist = getCurrentMonthEarnings()
app.layout = html.Div([
    dcc.Dropdown(
        id='symbol-dropdown',
        options=[
            {'label':str(i), 'value':i[0]} for i in alist #df['symbol'].unique()
        ],
        style={'width': '300px'},
    ),
    html.Div(id='dd-output-container')
    ])


@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('symbol-dropdown', 'value')])
def update_output(value):
    if value is not None:
        app.layout = html.Div([
            html.A(value, href='https://seekingalpha.com/symbol/'+value+'/earnings', target="_blank")
        ])

        return html.Div([
            html.A(value, href='https://seekingalpha.com/symbol/'+value+'/earnings', target="_blank")])


if __name__ == '__main__':
    app.run_server(debug=True)