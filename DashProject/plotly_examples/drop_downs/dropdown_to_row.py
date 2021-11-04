import pandas as pd
import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
available_indicators = df['State'].unique()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options = [{'label': i, 'value': i} for i in available_indicators],
        value='Texas'),
    dash_table.DataTable(id='my-datatable')
])
dt = datetime.now()
app.layout = html.Div([
    f'Date: {dt:%m-%d-%Y}',
    dcc.Dropdown(
        id='my-dropdown',
        options=[{'label': i, 'value': i} for i in available_indicators],
        value='Texas'),
    dash_table.DataTable(
    id='my-datatable',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'))
])

@app.callback(Output('my-datatable', 'selected_rows'), [Input('my-dropdown', 'value')])
def update_rows(selected_value):
    print(selected_value)
    #dff = df[df['Number of Solar Plants'] == selected_value]
    dff = df[df['State'] == selected_value]
    #print(dff)
    return dff.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
