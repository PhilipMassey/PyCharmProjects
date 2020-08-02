import pandas as pd
import robin_stocks as r

def getEarnings(positions):
    #symbols = list(map(lambda e: e.upper(), symbols))
    current_year_dates = []
    for symbol in positions:
        try:
            earnings = r.get_earnings(symbol=symbol)
            # print(earnings)
            if len(earnings) > 0:
                # current_year = list(filter(lambda e:e['year']==2020, earnings))
                earnings = list(filter(lambda e: e['report'] != None, earnings))
                current_year = list(filter(lambda e: e['report']['date'][0:4] == '2020', earnings))
                earnings_dates = list(map(lambda e: e['report']['date'], current_year))
                earnings_dates = list(filter(lambda e: e[5:7] > '05', earnings_dates))
                # print(earnings_date)
                current_year_dates.append((symbol, earnings_dates))
            else:
                print(symbol, 'no earnings')
        except Exception as e:
            print('skipped', symbol, e)

    current_year_dates = sorted(current_year_dates, key=lambda x: x[1][0])
    for e in current_year_dates:
        print(e[0], '\t', e[1])
