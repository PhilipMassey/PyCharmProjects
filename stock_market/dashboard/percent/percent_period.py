import market_data as md
import performance as pf
import pandas as pd
import dash
from dash import dash_table

ndays_range = md.get_perc_change_ndays()
df = pf.df_percents_for_range(ndays_range, ports=[md.sector_xl_etf])
print()

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    sort_action="native",
    sort_mode="multi",

)

if __name__ == '__main__':
    app.run_server(debug=True)
