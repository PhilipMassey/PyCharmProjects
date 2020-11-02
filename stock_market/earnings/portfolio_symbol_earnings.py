import pandas as pd
import portfolio as pf
import robin_stocks as r
import rh
r = rh.r

def getEarningsCurrentMonth(symbol,year,month):
    year_month = year+'-'+month
    earnings = r.get_earnings(symbol=symbol)
    if len(earnings) > 0:
        report_dicts = list(filter(lambda e: e['report'] != None, earnings))
        #print(symbol,report_dict)
        year_month_dicts = list(filter(lambda e: e['report']['date'][0:7] == year_month, report_dicts))
        year_month_date = list(map(lambda e: e['report']['date'], year_month_dicts))
        if len(year_month_date) > 0:
            #print(symbol,year_month_date)
            return symbol,year_month_date[0]

df_port = pf.getPortfolios()
symbols = pf.getPortfoliosSymbols()
year = '2020'
month = '11'

earnings = [getEarningsCurrentMonth(e,year,month) for e in symbols]
symbols_earnings = [e for e in earnings if e != None]
df = pd.DataFrame(symbols_earnings,columns=['symbol','earnings'])

df.set_index('symbol',inplace=True)
df_port_earnings = pd.concat([df,df_port],axis=1)
df_port_earnings.reset_index(inplace=True)
df_port_earnings.rename(columns={'index':'symbol','portfolio':'portfolio'},inplace=True)
df_port_earnings.dropna(inplace=True)
df_port_earnings=df_port_earnings[['earnings','portfolio','symbol']]
pd.set_option('display.max_rows', 500)
print(df_port_earnings.sort_values(by=['earnings',['portfolio']))