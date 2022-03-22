import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

radios_block = dcc.RadioItems(
    id = 'radio-block',
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='NYC',
    labelStyle={'display': 'block'}
)

radios_inline = dcc.RadioItems(
    id = 'radio-inline',
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='SF',
    labelStyle={'display': 'inline-block'}

)
label_block = html.Label('Radio Block',style={'font-size':'20px','font-family':'Arial'})
output_radio_block = html.Div(id='output-radio-block')
label_inline = html.Label('Radio Inline',style={'font-size':'20px','font-family':'Arial'})
output_radio_inline = html.Div(id='output-radio-inline')

block_1 = html.Div([label_block, radios_block, output_radio_block],
                style={'width':'50%','height':'100px', 'float':'left', 'background': 'green'})

block_2 = html.Div([label_inline, radios_inline, output_radio_inline],
                style = {'margin-left': '50%', 'height': '100px', 'background': 'blue'})



app.layout = html.Div([block_1, block_2])
#app.layout = html.Div([radios_block, output_radio_block, radios_inline, output_radio_inline])


# @app.callback([Output('block-out', 'children')],
#               [Input('radio-block','value')])
# def show_me(value):
#     return 'radio-block is: ' + value

@app.callback(
    Output('output-radio-block', 'children'),
    [Input('radio-block', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('output-radio-inline', 'children'),
    [Input('radio-inline', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.run_server(debug=True)