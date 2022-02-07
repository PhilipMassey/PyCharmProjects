import dash
from dash import html
from dash import dcc
from dash import dash_table as dt
from dash.dependencies import Output, Input
import market_data as md
import performance as pf

label_size = '18px'

results_date = html.Div('Current date',id='results-date',
                        style={'width': '100%', 'text-align': 'center','font-size':label_size})

label_perc_or_mean = html.Label('Perc or Mean',style={'font-size':label_size})
radio_perc_or_mean = html.Div([
    dcc.RadioItems(
        id='radio-perc-or-mean',
        options=[
            {'label': 'Portfolio Mean', 'value': pf.mean_option},
            {'label': 'Symbol percent change', 'value': pf.perc_option}
            ],
       labelStyle={'display': 'block'},
       value=pf.perc_option, ),
])


label_ndays_range = html.Label('Select Period', style={'font-size':label_size})
radio_ndays_range = html.Div([
    dcc.RadioItems(
        id='radio-ndays-range',
        options=[
            {'label': '5, 10, 21, 64, 128, 252 days', 'value': pf.calc_percent_year},
            {'label': '2 Months', 'value': pf.calc_percent_2monthly},
            {'label': '1 Month', 'value': pf.calc_percent_monthly}
        ],
        labelStyle={'display': 'block'},
        value=pf.calc_percent_year, ),
])


label_calc_percent = html.Label('Calc percent', style={'font-size':label_size})
radio_calc_percent = html.Div([
    dcc.RadioItems(
        id='radio-calc-percent',
        options=[
            {'label': 'Calc overall', 'value': pf.calc_interval_overall},
            {'label': 'Calc between', 'value': pf.calc_interval_between}
        ],
        labelStyle={'display': 'block'},
        value=pf.calc_interval_overall, ),
])


perc_or_mean_block = html.Div([label_perc_or_mean, radio_perc_or_mean],
                         style={'width': '33%', 'display': 'inline-block'})
ndays_range_block = html.Div([label_ndays_range, radio_ndays_range],
                             style={'width': '33%', 'display': 'inline-block'})
calc_interval_block = html.Div([label_calc_percent, radio_calc_percent],
                               style={'width': '33%', 'display': 'inline-block', 'float': 'right'})

dirs = md.get_portfolio_dirs()
dropdowns = html.Div([
        html.Div([
            html.Label('Portfolio Directories'),
            dcc.Dropdown(id='dropdown-dirs', options=[{'label': i, 'value': i} for i in dirs], value=None)],
            style={'width': '49%', 'float': 'left'}
            ),
    html.Div([
       html.Label('Portfolios'),
        dcc.Dropdown(id='dropdown-ports', options=[], value=None)],
        style = {'width': '49%','float': 'right'}
    ),

], style= {'width': '100%','display': 'inline-block'})

results_table = html.Div(id="results-table")


app = dash.Dash(__name__)
app.layout = html.Div([results_date, perc_or_mean_block, ndays_range_block, calc_interval_block, dropdowns, results_table])


#callback on directory selection
@app.callback(
    Output('dropdown-ports', 'options'),
    [Input('dropdown-dirs', 'value')])
def update_dropdown_ports(value):
    if(value != None):
        df_port_symbols = md.get_dir_port_symbols(value)
        return [{'label': i, 'value': i} for i in sorted(df_port_symbols["portfolio"].unique())]
    else:
        return []


#update table based on
@app.callback(
    Output('results-date','children'),
    Output('results-table', 'children'),
    Input('radio-calc-percent', 'value'),
    Input('radio-ndays-range', 'value'),
    Input('radio-perc-or-mean', 'value'),
    Input('dropdown-dirs', 'value'),
    Input('dropdown-ports', 'value')
)
def update_table(calc_percent, ndays_range, perc_or_mean, directory, port):
    results_date_value = 'No results'
    import pandas as pd
    df = pd.DataFrame({'options':[ndays_range, calc_percent], 'portfolios':[directory, port]})
    #ndays_range = md.get_ndays_periods(months=list(range(6,0,-1)))
    if ndays_range == pf.calc_percent_2monthly:
        ndays_range = md.get_ndays_periods(months=list(range(12, 0, -2)))
    elif ndays_range == pf.calc_percent_monthly:
        ndays_range = md.get_ndays_periods(months=list(range(6, 0, -1)))
    elif ndays_range == pf.calc_percent_year:
        ndays_range = md.get_ndays_periods(months=(12,6,3,1),weeks=(2,1))
    if perc_or_mean == pf.perc_option:
        df = pf.df_closing_percent_change(ndays_range, calc_percent, directory, port)
    elif perc_or_mean == pf.mean_option:
        df = pf.df_dir_ports_means_for_range(ndays_range, directory)
    return (md.get_date_for_ndays(ndays_range[-1])
,
            dt.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            style_cell={
                'font_family': 'arial',
                'font_size': '20px',
                'text_align': 'center'
            },
            sort_action='native'))

if __name__ == "__main__":
    app.run_server(debug=True)


