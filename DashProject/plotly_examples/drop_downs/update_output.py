import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

df = pd.DataFrame({
    'student_id': range(1, 11),
    'score': [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='score',
        options=[{'label': i, 'value': i} for i in range(1, 6)],
        value=1
    ),
    'was scored by this many students:',
    html.Div(id='output'),
])


@app.callback(Output('output', 'children'), Input('score', 'value'))
def update_output(value):
    filtered_df = df[df['score'] == value]
    return len(filtered_df)


if __name__ == '__main__':
    app.run_server(debug=True)
