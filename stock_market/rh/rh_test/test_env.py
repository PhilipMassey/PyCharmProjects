import sys; print('Python %s on %s' % (sys.version, sys.platform))
print('sys.path\t\t{},sep=\n'.format( sys.path))


import site;
print('Site packages\t\t{}'.format(site.getsitepackages()))

import robin_stocks as r
import inspect
print("Inspect getfile r\t{}".format( inspect.getfile(r)))
