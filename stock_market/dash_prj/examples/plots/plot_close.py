import dash
from dash import dcc
from dash import html
from datetime import datetime as dt
import yfinance as yf
from dash.dependencies import Input, Output
#app = dash.Dash('Hello World')

app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    start = '2020-01-01'
    end  = '{:%Y-%m-%d}'.format(dt.today())
    df = yf.download(tickers = selected_dropdown_value,interval = "1d",start=start,end=end,group_by = 'column',auto_adjust = True,prepost = False,threads = True)
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 'bWLwgP.css': 20, 'b': 30}}
    }


if __name__ == '__main__':
    app.run_server(debug=True, port=1052)