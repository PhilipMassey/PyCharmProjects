import portfolio as pf
import plots as pl

six = (360,60)
five = (270,45)
four=(180,30)
three = (90,15)
two = (60,10)
one = (30, 5)
half = (15,3)
quarter = (8,1)
period ,interval = one
account='Seeking Alpha'
dfall = pf.getSymPortPercPeriodsFltrd(period, interval, account)
pl.plotSymPercPerdiod(dfall,account,'bubble')
df = pf.aggregateOnPortfolio(dfall)
pl.plotPortPercPeriods(df,account,'bar')
