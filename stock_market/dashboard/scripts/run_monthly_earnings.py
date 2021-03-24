import sys;sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])
from dashboard import months_earnings
print('starting')
if __name__ == '__main__':
    months_earnings.app.run_server(debug=True)