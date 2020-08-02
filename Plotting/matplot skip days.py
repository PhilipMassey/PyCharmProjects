import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import matplotlib.cbook as cbook
from matplotlib.dates import bytespdate2num, num2date


datafile = cbook.get_sample_data('msft.csv', asfileobj=False)
print('loading %s' % datafile)
msft_data = np.genfromtxt(datafile, delimiter=',', names=True,
                          converters={0: bytespdate2num('%d-%b-%y')})[-40:]

#r = mlab.csv2rec('../data/aapl.csv')
r = msft_data
r.sort()
r = r[-30:]  # get the last 30 days

N = len(r)
ind = np.arange(N)  # the evenly spaced plot indices

def format_date(x, pos=None):
    thisind = np.clip(int(x+0.5), 0, N-1)
    return r.date[thisind].strftime('%Y-%m-%d')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ind, r.Close, 'o-')
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
fig.autofmt_xdate()

plt.show()