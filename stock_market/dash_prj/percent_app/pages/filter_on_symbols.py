import dash
dash.register_page(__name__)
from dash import callback
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from dash import dash_table as dt

import market_data as md
import pandas as pd

Holding = md.get_port_and_symbols('Holding')
holding_portfolios = Holding['portfolio'].unique()
layout = html.Div(
    [
        dcc.Input(id="input-symbol", type="text", placeholder="", debounce=True),
        html.Div(id='output-symbol'),
        html.Div(id="listing-table")
    ]
    )


@callback(
    Output('output-symbol','children'),
    Output('listing-table', 'children'),
    Input('input-symbol', 'value')
)
def update_table(symbol):
    print(symbol)
    if symbol == None or len(symbol) == 0:
        df = pd.DataFrame({'Status': ['depends']})
    else:
        symbol = symbol.upper()
        print(symbol)
        portfolios_symbols = md.get_port_and_symbols(directory=md.all)
        portfolios_with_symbols = portfolios_symbols[portfolios_symbols['symbol'] == symbol]['portfolio']
        dct = {'Listed': [port for port in portfolios_with_symbols if port not in holding_portfolios],
               'Holding': [port for port in portfolios_with_symbols if port in holding_portfolios]}
        df = pd.DataFrame.from_dict(dct, orient='index')
        df = df.T
        print(df)
    return (symbol,dt.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            style_cell={
                'font_family': 'arial',
                'font_size': '20px',
                'text_align': 'center'
            },
            sort_action='native'))




if __name__ == "__main__":
    app.run_server(debug=True,port=8001)