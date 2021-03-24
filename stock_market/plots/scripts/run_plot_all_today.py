import portfolio as pf
import plots as pl

six = (360,60)
five = (270,45)
four=(180,30)
three = (90,15)
two = (60,10)
month = (20, 5)
fortnight = (10,2)
week = (5,1)
period ,interval = month

dfall = pf.getTodaySymPortPercPeriodsFltrd(period, interval, excl_vol=True, excl_low_vol=True)
title = 'Seeking Alpha Periods Ending Today'
pl.plotSymPercPerdiod(dfall,title,'bubble')
df = pf.aggregateOnPortfolio(dfall)
pl.plotPortPercPeriods(df,title,'bar')

account = 'fidelity'
df = pf.filterdfbyAccountSymbols(dfall,account)
pl.plotSymPercPerdiod(df,account,'bubble')

account = 'm1finance'
df = pf.filterdfbyAccountSymbols(dfall,account)
pl.plotSymPercPerdiod(df,account,'bubble')
