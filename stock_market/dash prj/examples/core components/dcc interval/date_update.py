import dash
from dash import dash_table as dt
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from datetime import datetime
import dash_bootstrap_components as dbc


app = dash.Dash(__name__)

latest_sec = datetime.now()

date_div = html.Div([html.H1(datetime.now().strftime('%Y-%m-%d %H-%M:%S'),
                             style= {'opacity': '1','color': 'white', 'fontSize': 14}),
                     html.H1( id='a-title',
                             children = 'The latest_sec variable is: ' + latest_sec.strftime('%Y-%m-%d %H:%M:%S'),
                             style={'opacity': '1','color': 'white', 'fontSize': 14}),
                     ])


date_div2 = html.Div([
    html.Div(id='live-update-text',
             style={'font-size': '15px'}),
    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
    )
])

last_time = html.Div([
        "Input: ",
        dcc.Input(id='my-input', value=latest_sec, type='text'),
        html.Div(id='my-output')])

app.layout = html.Div([date_div, date_div2, last_time])


@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_date(n):
    global latest_sec
    latest_sec = datetime.now()
    return [html.Div(' dcc.Interval updated ' + latest_sec.strftime('%Y-%m-%d %H-%M:%S'))]

@app.callback([
    Output('my-output', 'children'),
    Output('a-title', 'children')],
    [Input('my-input', 'value')])
def go_on_them(input_value):
    a = 'Youve entered text ' +  f'{latest_sec:%Y-%m-%d %H-%M:%S}'
    return a,a


if __name__ == '__main__':
    app.run_server(debug=True)
