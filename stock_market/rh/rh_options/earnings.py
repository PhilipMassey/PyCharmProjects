import pandas as pd
import robin_stocks as r


def fltrempty(e):
    return True if len(e[1]) > 0 else False


def getEarnings(positions):
    # symbols = list(map(lambda e: e.upper(), symbols))
    current_year_dates = []
    for symbol in positions:
        try:
            earnings = r.get_earnings(symbol=symbol)
            # print(earnings)
            if len(earnings) > 0:
                # current_year = list(filter(lambda e:e['year']==2020, earnings))
                earnings = list(filter(lambda e: e['report'] != None, earnings))
                current_year = list(filter(lambda e: e['report']['date'][0:4] == '2021', earnings))
                earnings_dates = list(map(lambda e: e['report']['date'], current_year))
                earnings_dates = list(filter(lambda e: e[5:7] > '00', earnings_dates))
                # print(earnings_date)
                current_year_dates.append((symbol, earnings_dates))
            else:
                print(symbol, 'no earnings')
        except Exception as e:
            print('skipped', symbol, e)

        current_year_dates = list(filter(fltrempty, current_year_dates))
        current_year_dates = sorted(current_year_dates, key=lambda x: x[1][0])
    return current_year_dates
