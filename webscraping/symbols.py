import sys
print('Python version is {} running on platform {}'.format(sys.version, sys.platform))
print(*sys.path, sep='\n')
