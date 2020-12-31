#!/usr/bin/python

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/philipmassey/PycharmProjects/stock_market'])
#
# import importlib
#
# moduleName = input('Enter module name:')
# importlib.import_module(moduleName)
exec(open("/Users/philipmassey/PycharmProjects/stock_market/plots/scripts/script_plot_sa.py").read())
exec(open("/Users/philipmassey/PycharmProjects/stock_market/plots/scripts/script_plot_fidelity.py").read())
exec(open("/Users/philipmassey/PycharmProjects/stock_market/plots/scripts/script_plot_folio.py").read())
exec(open("/Users/philipmassey/PycharmProjects/stock_market/plots/scripts/script_plot_m1.py").read())
exec(open("/Users/philipmassey/PycharmProjects/stock_market/plots/scripts/script_plot_schwab.py").read())

