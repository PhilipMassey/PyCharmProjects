import portfolio as pf
import plots as pl

six = (360,60)
five = (270,45)
four=(180,30)
three = (90,15)
two = (60,10)
one = (30, 1)
half = (15,1)
quarter = (8,2)
period ,interval = half
account='Schwab'
dfa = pf.getSymPortPercPeriodsLowVty(period,interval,account)
pl.plotSymPercPerdiod(dfa,account,'bubble')
pl.plotSymPercPerdiod(dfa,account,'barsymbol')
