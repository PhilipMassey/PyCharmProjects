import dash
from dash import html
from dash import dcc
from dash import dash_table as dt
from dash.dependencies import Output, Input

label_perc_or_mean = html.Label('Percent calculation',style={'font-size':'20px'})

label_ndays_range = html.Label('Select Period', style={'font-size': '20px'})

label_calc_percent = html.Label('Calc percent', style={'font-size':'20px'})

perc_or_mean_block = html.Div([label_perc_or_mean],
                              style={'width': '33%', 'display': 'inline-block'})
ndays_range_block = html.Div([label_ndays_range],
                             style={'width': '33%', 'display': 'inline-block'})
calc_interval_block = html.Div([label_calc_percent],
                            style={'width': '33%', 'display': 'inline-block', 'float': 'right'})


app = dash.Dash(__name__)
app.layout = html.Div([perc_or_mean_block, ndays_range_block, calc_interval_block],style = {'class':'row'})



if __name__ == "__main__":
    app.run_server(debug=True,port=1521)