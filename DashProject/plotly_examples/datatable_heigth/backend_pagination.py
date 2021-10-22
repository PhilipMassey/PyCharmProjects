import dash
from dash import dash_table
import pandas as pd
from collections import OrderedDict

app = dash.Dash(__name__)

df = pd.DataFrame(OrderedDict(
    [
        [
            'Column {}'.format(i + 1), list(range(130))
        ] for i in range(15)
    ]
))

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    virtualization=True,
    fixed_rows={'headers': True},
    style_cell={'minWidth': 95, 'width': 95, 'maxWidth': 95},
    style_table={'height': 300}  # default is 500
)

if __name__ == '__main__':
    app.run_server(debug=True)