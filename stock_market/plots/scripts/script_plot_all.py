import portfolio as pf
import plots as pl

six = (360,60)
five = (270,45)
four=(180,30)
three = (90,15)
two = (60,10)
one = (30, 3)
half = (15,2)
quarter = (8,1)
period ,interval = quarter

dfall = pf.getSymPortPercPeriodsFltrd(period, interval)
title = 'Seeking Alpha'
pl.plotSymPercPerdiod(dfall,title,'bubble')
df = pf.aggregateOnPortfolio(dfall)
pl.plotPortPercPeriods(df,title,'bar')

account = 'fidelity'
df = pf.filterdfbyAccountSymbols(dfall,account)
pl.plotSymPercPerdiod(df,account,'bubble')

account = 'm1finance'
df = pf.filterdfbyAccountSymbols(dfall,account)
pl.plotSymPercPerdiod(df,account,'bubble')

account = 'folio'
df = pf.filterdfbyAccountSymbols(dfall,account)
pl.plotSymPercPerdiod(df,account,'bubble')