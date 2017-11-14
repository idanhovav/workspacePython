import sys
try:
	import setuptools
except ImportError:
	print('1')
	sys.exit(1)
else:
	print('0')
	sys.exit(0)