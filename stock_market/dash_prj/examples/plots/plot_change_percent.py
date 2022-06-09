import dash
from dash import dcc
from dash import html
from datetime import datetime as dt
import market_data as md
import performance as pf
from dash.dependencies import Input, Output
#app = dash.Dash('Hello World')
import plotly.express as px
import plotly.graph_objs as go

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
    calc_percent = pf.calc_interval_overall
    opt_ndays_range = pf.calc_percent_year
    ndays_range = pf.get_ndays_range(opt_ndays_range)
    directory='holding'
    port = 'SA New'
    symbols = md.get_symbols_dir_or_port(directory=directory, port=port)
    df = pf.df_calc_percent_change_zero(ndays_range, calc_percent, symbols)
    fig = px.line(df, x=df.index.values, y=df.columns.values)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port=1052)