import pandas as pd
import dash
from dash import dash_table as dt
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv', header=0, encoding = 'utf8')

app = dash.Dash()
application = app.server

dropdown = html.Div([
    html.Label('State'),
    dcc.Dropdown(id='dropdown_d1', options=[{'label': i, 'value': i} for i in df["State"].unique()], value=None),
    html.Label('address'),
    dcc.Dropdown(id='dropdown_d2', options=[], value=None)
])


#its better to have a Div here so that you can update the entire div in the callback and add the necessary properties in the callback
final_table = html.Div(id="final_table")

app.layout = html.Div([dropdown, final_table])


#callback to update second dropdown based on first dropdown
#This callback is used to update the second dropdown based on the value selected in the first dropdown so that its dynamically updated (this is a good  practice rather than having a static list of options).
@app.callback(Output('dropdown_d2', 'options'),
          [
            Input('dropdown_d1', 'value'),
          ])
def update_dropdown_2(d1):
    print(d1)
    if(d1 != None):
        df_filtered = df[(df["State"]==d1)]
        return [{'label': i, 'value': i} for i in df_filtered["State"].unique()]
    else:
        return []


#this callback to update the final table should be based on both the input dropdown values, so the input parameters are two dropdown_d1, dropdown_d2
#based on these values filter the dataframe and update the table
#since dataframe is a global declaration you don't need to again consume it here.
@app.callback(Output('final_table', 'children'),
          [
            Input('dropdown_d1', 'value'),
            Input('dropdown_d2', 'value'),
          ])
def update_table(d1, d2):

    if(d1 != None):  # and d2 != None):
         df_filtered = df[(df["State"]==d1)] # & (df["Address"]==d2)]
    else:
        df_filtered = df
    return [dt.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df_filtered.columns],
        data=df_filtered.to_dict('records'))]
#        )]
#     else:
#         print("none")
#         return []


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)