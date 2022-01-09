import dash
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output, State
from dash import dcc
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
# style_sheets = ['/assets/custom.css']app = dash.Dash(__name__, external_stylesheets=style_sheets)

app = dash.Dash(__name__)

msg_one = html.Div([
    dcc.Textarea(
        id='msg_one',
        value='Hello'
        #style={'width': '100%', 'height': 300},
    ),
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
])

adiv = html.Div(id='output_div')

data_table = html.Div([
    dash_table.DataTable(
        id='table-one',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=[df.to_dict('records')])
])

datatable = html.Div([
    dash_table.DataTable(
        id='data_table',
        columns=[{
            'name': 'Column {}'.format(i),
            'id': 'column-{}'.format(i),
        } for i in range(1, 5)],
        data=[
        {'column-{}'.format(i): (j + (i-1)*5) for i in range(1, 5)}
        for j in range(5)
        ]
    ),
    html.Div(id='output_div')
])

@app.callback(
    Output('output_div', 'children'),
    Input('data_table', 'active_cell'),
    State('data_table', 'data')
)
def getActiveCell(active_cell, data):
    if not active_cell:
        return df.iloc[0, 0]
    if active_cell:
        col = active_cell['column_id']
        row = active_cell['row']
        cellData = data[row][col]
        return html.P(f'row: {row}, col: {col}, value: {cellData}')
    return html.P('no cell selected')

@app.callback(Output('selected-letter', 'children'),
              [Input('table-one', 'active_cell'),
               Input('table-one', 'data')])
def get_active_letter(active_cell, data):
    if not active_cell:
        return df_1.iloc[0,0]
    if active_cell:
        return str(data[active_cell[0]]['Letter'])


app.layout = html.Div(msg_one, adiv, datatable)




if __name__ == '__main__':
    app.run_server(debug=True)