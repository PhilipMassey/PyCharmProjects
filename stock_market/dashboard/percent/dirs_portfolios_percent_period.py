import pandas as pd
import dash
from dash import dash_table as dt
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import market_data as md
import performance as pf
from datetime import datetime


app = dash.Dash()
application = app.server


date_div = html.Div(id='date_div')

radio_value_period = 'monthly'
radio_period = html.Div([
    dcc.RadioItems(
        id='radio-button-period',
        options=[
            {'label': '5, 10, 21, 64, 128, 252', 'value': 'wfm3612_option'},
            {'label': 'Monthly Percent', 'value': 'monthly'}
            ],
        labelStyle={'display': 'inline_block'},
        value='monthly', ),
    html.P(id = 'output-text-period')
])

radio_value_measure = 'MEAN'
radio_measure = html.Div([
    dcc.RadioItems(
        id='radio-button-measure',
        options=[
            {'label': 'Portfolio Mean', 'value': 'MEAN'},
            {'label': 'Symbol Percent', 'value': 'PERC'}
            ],
       labelStyle={'display': 'inline_block'},
       value='PERC', ),
    html.P(id = 'output-text-measure')
])


dirs = md.get_portfolio_dirs()
today = f'Date: {datetime.now():%m-%d-%Y}'
dropdown = html.Div([
    html.Label('Directories'),
    dcc.Dropdown(id='dropdown_d1', options=[{'label': i, 'value': i} for i in dirs], value=None),
    radio_measure,
    html.Label('Portfolio'),
    dcc.Dropdown(id='dropdown_d2', options=[], value=None),
    dcc.Interval(
        id='interval-component',
        interval=8640000,  # in milliseconds
        n_intervals=0
    )
])


#its better to have a Div here so that you can update the entire div in the callback and add the necessary properties in the callback
final_table = html.Div(id="final_table")


app.layout = html.Div([date_div, dropdown, radio_period, final_table])


#callback on radio-button-measure
@app.callback(Output('output-text-measure', 'children'),
              [Input('radio-button-measure', 'value')])
def radio_value_measure(value):
    global radio_value_measure
    radio_value_measure = value
    return radio_value_measure


#callback on radiobutton-period
@app.callback(Output('output-text-period', 'children'),
              [Input('radio-button-period', 'value')])
def update_graph(value):
    global radio_value_period
    radio_value_period = value
    return ''

#callback to update second dropdown based on first dropdown
@app.callback(Output('dropdown_d2', 'options'),
          [Input('dropdown_d1', 'value')])
def update_dropdown_2(d1):
    if(d1 != None):
        df_port_symbols = md.get_dir_port_symbols(d1)
        return [{'label': i, 'value': i} for i in sorted(df_port_symbols["portfolio"].unique())]
    else:
        return []


# dataframe is a global declaration you don't need to again consume it here.
@app.callback(Output('final_table', 'children'),
          [
            Input('dropdown_d1', 'value'),
            Input('dropdown_d2', 'value'),
          ])
def update_table(d1, d2):
    global today
    today = f'Date: {datetime.now():%m-%d-%Y}'
    if radio_value_period == 'monthly':
        ndays_periods = md.get_ndays_range_montlhly()
        df_filtered = pf.df_percents_between_days(ndays_periods, ports=[d2], db_coll_name=md.db_close)
    else:
        ndays_range = md.get_ndays_range_wfm3612()
        if radio_value_measure == 'PERC':
            if d1 != None and d2 == None:
                dfd = md.get_dir_port_symbols(d1)
                symbols = list(dfd['symbol'].values)
                df_filtered = pf.df_percents_for_range(ndays_range, symbols=symbols)
            elif (d2 != None):  # and d2 != None):
                 df_filtered = pf.df_percents_for_range(ndays_range, ports=[d2])
            else:
                #df_filtered = df
                df_filtered = pf.df_percents_for_range(ndays_range)
        else:
            df_filtered = pf.df_dir_ports_means_for_range(ndays_range, d1).round(decimals=2)
    return [dt.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df_filtered.columns],
    data=df_filtered.to_dict('records'),
    style_cell={
        'font_family': 'arial',
        'font_size': '20px',
        'text_align': 'center'
    },
    sort_action='native')]


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)