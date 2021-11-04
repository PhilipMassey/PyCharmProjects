import dash
import pandas as pd
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
available_indicators = df['State'].unique()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in available_indicators],
        value='Texas'),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    )
])


@app.callback(
    Output('table', 'selected_rows'),
    [Input('dropdown', 'value')])
def update_rows(selected_value):
    print('selected_value', selected_value)
    dff = df[df['State'] == selected_value]
    #print(dff)
    return dff.to_dict('records')


def update_rows(selected_value):
    data = df[df['State'] == selected_value]
    columns = [{'name': i, 'id': i} for i in data.columns]
    return [dt.DataTable(data=data, columns=columns)]

def update_table(d1):
    if(d1 != None):  # and d2 != None):
         df_filtered = df[(df["State"]==d1)] # & (df["Address"]==d2)]
    else:
        df_filtered = df
    return [dt.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df_filtered.columns],
        data=df_filtered.to_dict('records'))]

if __name__ == '__main__':
    app.run_server(debug=True)
