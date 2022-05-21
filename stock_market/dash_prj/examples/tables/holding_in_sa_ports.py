import dash
from dash import callback
from dash import html
from dash import dcc
from dash import dash_table
from dash.dependencies import Output, Input
import market_data as md
import performance as pf
import pandas as pd
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash_extensions import EventListener
import webbrowser

def int_to_en(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty'}
    return d[num]

def df_holding_in_sa_ports():
    sa_ports = md.sa_ports
    sa_ports.append(md.sc_port)
    holding = md.get_symbols('Holding')
    dct = {}
    for port in sa_ports:
        quant = md.get_symbols_for_portfolios([port])
        symbols = sorted(set(holding).intersection(set(quant)))
        #print(port, ': ', symbols)
        dct[port] = symbols
    df = pd.DataFrame.from_dict(dct, orient='index')
    df.columns = [int_to_en(column) for column in df.columns]
    df.reset_index(inplace=True)
    df.rename(columns={'index':'port'},inplace=True)
    return df
df = df_holding_in_sa_ports()


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# table = dash_table.DataTable(
#     id="tbl",
#     data=df.to_dict("records"),
#     columns=[{"name": i, "id": i} for i in df.columns],
# )
#



# app.layout = dbc.Container(
#     [
#         dbc.Label("Click a cell in the table:"),
#         listen_table,
#         dbc.Alert("Click the table", id="out"),
#         html.Div(id="event"),
#     ]
# )

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    style_cell={'textAlign': 'left'},
)

if __name__ == "__main__":
    app.run_server(debug=True, port=7676)
