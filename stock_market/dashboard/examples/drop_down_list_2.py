import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd




app = dash.Dash(__name__)
alist = ['AVNW','BMY','REGN','PCTY','BEP','CI','MRK','DX','CLSK','NUAN','AMKR','DAC ','IIVI','CGC ','AYX ','CNC']
df= pd.DataFrame({
    'symbol' : alist
    })
app.layout = html.Div([
    dcc.Dropdown(
        id='symbol-dropdown',
        options=[
            {'label':i, 'value':i} for i in alist #df['symbol'].unique()
        ],
        value='NYC',
        style={'width': '300px'},
    ),
    html.Div(id='dd-output-container')
    ])


@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('symbol-dropdown', 'value')])
def update_output(value):
    filtered_df = df[df['symbol'] == value]
    selected = filtered_df.iloc[0]['symbol']
    app.layout = html.Div([
        html.A(selected, href='https://seekingalpha.com/symbol/'+selected+'/earnings', target="_blank")
    ])

    return html.Div([
        html.A(selected, href='https://seekingalpha.com/symbol/'+selected+'/earnings', target="_blank")])


if __name__ == '__main__':
    app.run_server(debug=True)