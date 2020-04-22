import os
import sys
import site
os.putenv('PYTHONPATH','/Library/Frameworks/Python.framework/Versions/3.7/bin')

print(sys.path)
site.addsitedir('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages')
#print(sys.path)
# print('{0}\t{1}'.format('sys.prefix',sys.prefix))
# print('{0}\t{1}'.format('HOME', os.environ['HOME']))
print('{0}\t{1}'.format('PYTHONPATH', os.getenv('PYTHONPATH', 'PYTHONPATH not found')))

import pandas as pd
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=None,columns=('a','b','c'))
print(df)