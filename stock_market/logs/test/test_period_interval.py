import market_data as md

ndays_step = md.get_period_interval()
print(ndays_step)

ndays_step = md.get_period_interval(120)
print(ndays_step)

ndays_step = md.get_period_interval(30)
print(ndays_step)

ndays_step = md.get_period_interval(5)
print(ndays_step)