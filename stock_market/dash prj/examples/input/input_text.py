from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__)

ALLOWED_TYPES = (
    "text",
)


app.layout = html.Div(
    [
        dcc.Input(
            id='input1',
            type='text',
            placeholder="input type {}".format('text')),
        html.Div(id="output1"),
        dcc.Input(id="input2", type="text", placeholder="", debounce=True),
        html.Div(id="output2")
    ]
    )




@app.callback(
    Output("output1", "children"),
    Input("input1".format('text'), "value"),
)
def cb_render(value):
    return value

@app.callback(
    Output("output2", "children"),
    Input("input2".format('text'), "value")

)
def cb_render(value):
    return value



if __name__ == "__main__":
    app.run_server(debug=True,port=8001)