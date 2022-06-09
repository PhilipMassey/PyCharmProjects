import dash
dash.register_page(__name__, path="/plot-perc")
from dash import callback
from dash import html
from dash import dcc
from dash import dash_table as dt
from dash.dependencies import Output, Input
import market_data as md
import performance as pf
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import apis
label_size = '18px'

results_date = html.Div('Current date',id='results-date-p',
                        style={'width': '100%', 'text-align': 'center','font-size':label_size})


label_ndays_range = html.Label('Select Period', style={'font-size':label_size})
radio_ndays_range = html.Div([
    dcc.RadioItems(
        id='radio-ndays-range-p',
        options=[
            {'label': '5, 10, 21, 64, 128, 252 days', 'value': pf.calc_percent_year},
            {'label': '2 Months', 'value': pf.calc_percent_2monthly},
            {'label': '1 Month', 'value': pf.calc_percent_monthly},
            {'label': '2 Weeks', 'value': pf.calc_percent_2weekly},
            {'label': '1 Week', 'value': pf.calc_percent_weekly}
        ],
        labelStyle={'display': 'block'},
        value=pf.calc_percent_weekly, ),
])


label_calc_percent = html.Label('Calc percent', style={'font-size':label_size})
radio_calc_percent = html.Div([
    dcc.RadioItems(
        id='radio-calc-percent-p',
        options=[
            {'label': 'Calc overall', 'value': pf.calc_interval_overall},
            {'label': 'Calc between', 'value': pf.calc_interval_between}
        ],
        labelStyle={'display': 'block'},
        value=pf.calc_interval_between, ),
])


ndays_range_block = html.Div([label_ndays_range, radio_ndays_range],
                             style={'width': '33%', 'display': 'inline-block'})
calc_interval_block = html.Div([label_calc_percent, radio_calc_percent],
                               style={'width': '33%', 'display': 'inline-block', 'float': 'right'})

dirs = md.get_portfolio_dirs()
dropdowns = html.Div([
        html.Div([
            html.Label('Portfolio Directories'),
            dcc.Dropdown(id='dropdown-dirs-p', options=[{'label': i, 'value': i} for i in dirs], value=None)],
            style={'width': '49%', 'float': 'left'}
            ),
    html.Div([
       html.Label('Portfolios'),
        dcc.Dropdown(id='dropdown-ports-p', options=[], value=None)],
        style = {'width': '49%','float': 'right'}
    ),

], style= {'width': '100%','display': 'inline-block'})



dct_profile = apis.dct_mdb_symbol_names()
def get_tooltip(symbol):
    if symbol in dct_profile:
        return dct_profile[symbol][0]
    else:
        return 'No worries,mate!'

results_graph = dcc.Graph(
        id='results-graph-p')

#app = dash.Dash(__name__)
layout = html.Div([results_date,  ndays_range_block,
                   calc_interval_block, dropdowns,
                   results_graph]
                  )


#callback on directory selection
@callback(
    Output('dropdown-ports-p', 'options'),
    [Input('dropdown-dirs-p', 'value')])
def update_dropdown_ports(value):
    if(value != None):
        df_port_symbols = md.get_dir_port_symbols(value)
        return [{'label': i, 'value': i} for i in sorted(df_port_symbols["portfolio"].unique())]
    else:
        return []


#update table based on
@callback(
    Output('results-date-p', 'children'),
    Output('results-graph-p', 'figure'),
    Input('radio-calc-percent-p', 'value'),
    Input('radio-ndays-range-p', 'value'),
    Input('dropdown-dirs-p', 'value'),
    Input('dropdown-ports-p', 'value')
)
def update_graph(calc_percent, opt_ndays_range,  directory, port):
    results_date_value = 'No results'
    fig = px.line()
    if directory is None:
        ndays_range = md.get_ndays_periods(months=list(range(12, 0, -2)))
        df = pd.DataFrame({'directory':[directory], 'symbol':[port]})
    else:
        ndays_range = pf.get_ndays_range(opt_ndays_range)
        if directory == 'holding' or port is not None:
            symbols = md.get_symbols_dir_or_port(directory=directory, port=port)
            df = pf.df_calc_percent_change_zero(ndays_range, calc_percent, symbols)
            fig = px.line(df, x=df.index.values, y=df.columns.values)
    return (md.get_date_for_ndays(ndays_range[-1]),
            fig)



