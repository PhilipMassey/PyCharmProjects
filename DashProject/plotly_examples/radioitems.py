import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

aradio = html.Div([dcc.RadioItems(id='input-radio-button',
                                options=[
                                    {'label': 'New York City', 'value': 'NYC'},
                                    {'label': 'Montréal', 'value': 'MTL'},
                                    {'label': 'San Francisco', 'value': 'SF'}
                                ],
                                labelStyle={'display': 'block'},
                                value='MTL',),
                    html.P(id = 'output-text')])

app.layout = html.Div([aradio])


@app.callback(Output('output-text', 'children'),
              [Input('input-radio-button', 'value')])
def update_graph(value):
    print()
    return f'The selected value is {value}'


if __name__ == "__main__":
    app.run_server(debug=True, port=8081)