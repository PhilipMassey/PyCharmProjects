import dash
from dash import Dash, Input, Output, callback
from dash import dash_table as dt
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_csv('https://git.io/Juf1t')

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Label('Click a cell in the table:'),
    dt.DataTable(
        id='tbl', data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
    ),
    dbc.Alert("Click the table", id='tbl_out'),
])

@callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
def update_graphs(active_cell):
  return str(active_cell)

if __name__ == "__main__":
    app.run_server(debug=True)
