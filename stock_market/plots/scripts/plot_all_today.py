import sys; sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])
sys.path.extend(['/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages'])
import performance as pf
import plots as pl
import market_data as md


ndays_step=md.get_period_interval()  # defaults start to 2020/04/01
ndays_step=md.get_period_interval(20)
ndays_step=md.get_period_interval(10)

dfall = pf.getTodaySymPortPercPeriodsFltrd(ndays_step, incl=md.sa)
title = 'SA Industries and Sectors up to today'
title = '{} days,{} step - {}'.format(ndays_step[0],ndays_step[1],title)
df = pf.aggregateOnPortfolio(dfall)
pl.plotPortPercPeriods(df,title,'bar','portfolio')

dfall = pf.getTodaySymPortPercPeriodsFltrd(ndays_step, incl=md.watching)
title = 'Watching up to today'
title = '{} days,{} step - {}'.format(ndays_step[0],ndays_step[1],title)
df = pf.aggregateOnPortfolio(dfall)
pl.plotPortPercPeriods(df,title,'bar', 'portfolio')

#pl.plotSymPercPerdiod(dfall,title,'bubble')
