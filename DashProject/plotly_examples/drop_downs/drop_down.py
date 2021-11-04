import pandas as pd
import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'},
            {'label': 'Seattle', 'value': 'SEA'},
            {'label': 'Pittsburgh', 'value': 'PIT'}

        ],
        #value=['NYC','SEA'],
        placeholder="Select a city",
        multi=True
    ),
    html.Div(id='dd-output-container')
])


@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)