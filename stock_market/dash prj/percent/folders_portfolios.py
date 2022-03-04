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
dct_profile = md.dct_mdb_profile_directory_port()
def get_tooltip(symbol):
    if symbol in dct_profile:
        return dct_profile[symbol][0]
    else:
        return 'No worries,mate!'

app = dash.Dash()
application = app.server

results_date_value = f'Date: {datetime.now():%m-%d-%Y}'

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
def update_table(directory, port):
    results_date_value = 'No results'
    import pandas as pd
    if port is None:
        df = pd.DataFrame({'directory':[directory], 'symbol':[port]})
    else:
        ndays_range = md.get_ndays_periods(months=list(range(12, 0, -2)))
        calc_percent = pf.calc_interval_between
        df = pf.df_closing_percent_change(ndays_range, calc_percent, directory, port)
    return (dt.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            tooltip_data=[
                {
                    'symbol': {'value': get_tooltip(value), 'type': 'markdown'}
                    for column, value in row.items()
                } for row in df[['symbol']].to_dict('records')
            ],

        data=df.to_dict('records'),
            export_format="csv",
            style_cell={
                'font_family': 'arial',
                'font_size': '20px',
                'text_align': 'right'
            },
            style_cell_conditional=[
            {
                'if': {'column_id': 'portfolio'},
                'textAlign': 'left'
            },
                {'if': {'column_id': 'portfolio'},
                 'maxWidth': '250px'},
            ],
            sort_action='native'))

if __name__ == "__main__":
    app.run_server(debug=True, port=8051)