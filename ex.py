def divide_exact(n, d):
	"""Return the quotient and remainder of dividing N by D.

	>>> q, r = divide_exact(2015,10)
	>>> q
	201
	>>> r
	5
	"""
	return n // d , n % d

def absolute_value(x):
	""" Take the absolute value of x.
	>>> absolute_value(-3)
	3
	>>> absolute_value(0)
	0
	>>> absolute_value(3+22)
	25
	"""
	if x < 0:
		return -x
	elif x == 0:
		return 0
	else:
		return x

