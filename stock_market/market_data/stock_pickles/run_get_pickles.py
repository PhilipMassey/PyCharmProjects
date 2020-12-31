import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])

import market_data as md
def getRow(ndays):
    #print('{:d}'.format(ndays))
    df = md.getStockPickleNBDays(ndays)
    dt = md.getRowYmdDate(df)
    print('{:d} {}'.format(ndays,dt))

#[getRow(ndays) for ndays in range(237,360)]

import threading
import multiprocessing
if __name__ == '__main__':
     for i in range(361,377):
         p = multiprocessing.Process(target=getRow, args=(i,))
         #t = threading.Thread(target=getRow, args=(i,))
         p.start()
         p.join() # this line allows you to wait for processes

