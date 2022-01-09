import pandas as pd
import dash
from dash import dash_table as dt
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import market_data as md
import performance as pf
from os.path import isfile, join, isdir
from os import listdir
from datetime import datetime

dirs = sorted(d for d in listdir(md.data_dir) if isdir(join(md.data_dir, d)))

app = dash.Dash()
application = app.server

today = f'Date: {datetime.now():%m-%d-%Y}'

html.Br()
date_div = html.Div(id='date-output')
html.Br()


dropdown = html.Div([
    html.Label('Directories'),
    dcc.Dropdown(id='dropdown_d1', options=[{'label': i, 'value': i} for i in dirs], value=None),
    html.Label('Portfolio'),
    dcc.Dropdown(id='dropdown_d2', options=[], value=None),
    dcc.Interval(
        id='interval-component',
        interval=8640000,  # in milliseconds
        n_intervals=0
    )
])


final_table = html.Div(id="final_table")

app.layout = html.Div([date_div, dropdown, final_table])


#callback to update second dropdown based on first dropdown
@app.callback(Output('dropdown_d2', 'options'),
          [
            Input('dropdown_d1', 'value'),
          ])
def update_dropdown_2(d1):
    print(d1)
    if(d1 != None):
        df_port_symbols = md.get_dir_port_symbols(d1)
        return [{'label': i, 'value': i} for i in sorted(df_port_symbols["portfolio"].unique())]
    else:
        return []


@app.callback(Output('final_table', 'children'),
          [
            Input('dropdown_d1', 'value'),
            Input('dropdown_d2', 'value'),
          ])
def update_table(d1, d2):
    ndays_range = md.get_ndays_range_perc_days()
    if d1 != None and d2 == None:
        dfd = md.get_dir_port_symbols(d1)
        symbols = list(dfd['symbol'].values)
        df_filtered = pf.df_percents_for_range(ndays_range, symbols=symbols)
    elif (d2 != None):  # and d2 != None):
         df_filtered = pf.df_percents_for_range(ndays_range, ports=[d2])
    else:
        #df_filtered = df
        df_filtered = pf.df_percents_for_range(ndays_range)

    return [dt.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df_filtered.columns],
        data=df_filtered.to_dict('records'),
        sort_action='native')]


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)