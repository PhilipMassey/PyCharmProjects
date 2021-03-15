from datetime import datetime
import robin_stocks as r


def fltrempty(e):
    return True if len(e[1]) > 0 else False

def getYearMonthDay():
    today = datetime.today()
    (year, month,day) = (today.year, today.month,today.day)
    year = str(year)
    month = '{0:02d}'.format(month)
    day = '{0:02d}'.format(day)
    return year,month,day

def getEarnings(symbols,year,month):
    current_year_dates = []
    for symbol in symbols:
        try:
            earnings = r.get_earnings(symbol)
            # print(earnings)
            if len(earnings) > 0:
                earnings = list(filter(lambda e: e['report'] != None, earnings))
                current_year = list(filter(lambda e: e['report']['date'][0:4] == year, earnings))
                earnings_dates = list(map(lambda e: e['report']['date'], current_year))
                earnings_dates = list(filter(lambda e: e[5:7] == month, earnings_dates))
                current_year_dates.append((symbol, earnings_dates))
            else:
                print(symbol, 'no earnings')
        except Exception as e:
            print('skipped', symbol, e)

        current_year_dates = list(filter(fltrempty, current_year_dates))
        current_year_dates = sorted(current_year_dates, key=lambda x: x[1][0])
        current_month_date = [(x[0],x[1][0]) for x in current_year_dates]
    return current_month_date
