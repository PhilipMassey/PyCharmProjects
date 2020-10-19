from fastquant import get_pse_data, backtest
df = get_pse_data("JFC", "2018-01-01", "2019-01-01")
backtest('smac',df,fast_period=15,slow_period=40)