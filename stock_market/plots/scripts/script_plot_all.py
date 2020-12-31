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

dfall = pf.getSymPortPercPeriodsLowVty(period,interval)
pl.plotSymPercPerdiod(dfall,account,'bubble')
df = pf.aggregateOnPortfolio(dfall)
pl.plotPortPercPeriods(df,account,'bar')

account='Fidelity'
df = pf.filterdfbyAccountSymbols(dfall,account)
pl.plotSymPercPerdiod(df,account,'bubble')
pl.plotSymPercPerdiod(df,account,'barsymbol')

account='Folio'
df = pf.filterdfbyAccountSymbols(dfall,account)
pl.plotSymPercPerdiod(df,account,'bubble')
pl.plotSymPercPerdiod(df,account,'barsymbol')

account='M1'
df = pf.filterdfbyAccountSymbols(dfall,account)
pl.plotSymPercPerdiod(df,account,'bubble')
pl.plotSymPercPerdiod(df,account,'barsymbol')

account='Schwab'
df = pf.filterdfbyAccountSymbols(dfall,account)
pl.plotSymPercPerdiod(df,account,'bubble')
pl.plotSymPercPerdiod(df,account,'barsymbol')
