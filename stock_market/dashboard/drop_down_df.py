import dash
import dash_html_components as html
import dash_table
import pandas as pd
from collections import OrderedDict


app = dash.Dash(__name__)
app.title = 'Earnings'
app.layout = html.Div([
    dash_table.DataTable(
        id='table-dropdown',
        data=df.to_dict('records'),
        columns=[
            {'id': 'climate', 'name': 'climate', 'presentation': 'dropdown'},
            {'id': 'temperature', 'name': 'temperature'},
            {'id': 'city', 'name': 'city', 'presentation': 'dropdown'},
        ],

        editable=True,
        dropdown={
            'climate': {
                'options': [
                    {'label': i, 'value': i}
                    for i in df['climate'].unique()
                ]
            },
            'city': {
                 'options': [
                    {'label': i, 'value': i}
                    for i in df['city'].unique()
                ]
            }
        }
    ),
    html.Div(id='table-dropdown-container')
])


if __name__ == '__main__':
    app.run_server(debug=True)