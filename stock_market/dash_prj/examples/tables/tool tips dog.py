import dash
from dash import dash_table
import pandas as pd
from collections import OrderedDict
import market_data as md


data_election = OrderedDict(
    [
        (
            "Date",
            [
                "July 12th, 2013 - July 25th, 2013",
                "July 12th, 2013 - August 25th, 2013",
                "July 12th, 2014 - August 25th, 2014",
            ],
        ),
        (
            "Election Polling Organization",
            ["The New York Times", "Pew Research", "The Washington Post"],
        ),
        ("Rep", [1, -20, 3.512]),
        ("Dem", [10, 20, 30]),
        ("Ind", [2, 10924, 3912]),
        (
            "Region",
            [
                "AAPL",
                "SHY",
                "DXC",
            ],
        ),
    ]
)

df = pd.DataFrame(data_election)

app = dash.Dash(__name__)
dct = md.dct_symbol_name_directory_port()

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    tooltip_data=[
        {
            'Region': {'value': str(dct[value][0]), 'type': 'markdown'}
            for column, value in row.items()
        } for row in df[['Region']].to_dict('records')
    ],

    # Overflow into ellipsis
    style_cell={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0,
    },
    tooltip_delay=0,
    tooltip_duration=None
)


if __name__ == '__main__':
    app.run_server(debug=True, port=7001)

# tooltip_data=[
#         {
#             'Region': {'value': str(dct[symbol]), 'type': 'markdown'}
#             for symbol in df['Region']
#         }],