#Functions treat rationals as having numers and denoms
#use constructors and selecters from lower abstraction level
#Rational Arithmetic

def add_rational(a, b):
	"""Adds together two rational numbers by using their 
	nums and denominators along with basic arithmetic. """
	return rational((numer(a)*denom(b) + numer(b)*denom(a)),
	(denom(a) * denom(b)))

def mul_rational(x, y):
	"""Multiplies together two rational numbers by using their 
	numerators and denominators along with basic arithmetic."""
	return rational(numer(x) * numer(y) , denom(x) * denom(y))

def print_rational(x):
	"""Prints out the rational number. """
	print(numer(x), '/' , denom(x))

def are_equal(x, y):
	""" Returns boolean value of whether
	 rational numbers x & y are even"""
	nx, ny = numer(x), numer(y)
	dx, dy = denom(x), denom(y)
	return nx*dy == ny*dx
#===============================================================
#Abstraction Barrier
#Creates constructors and selectors in separate abstraction level,
#treating rationals as lists
#Constructors and Selectors
def rational(n, d):
	"""Constructs a rational number representing N/D simplified
	>>> rational(2,3)
	[2, 3]
	>>> rational(4,4)
	[1, 1]
	>>> rational(9,3)
	[3, 1]
	"""
	return  [(n//gcf(n,d)), (d//gcf(n,d))]

def numer(x):
	"""Returns numerator of a rational number x."""
	return x[0]

def denom(x):
	"""Returns denominator of rational number x."""
	return x[1]

#===============================================================
#Alternative Representation of Rationals
#Creates constructors and selectors in separate abstraction level,
#treating rationals as functions
#Constructors and Selectors
#def rational(n, d):
#	"""Constructs a rational number representing N/D simplified"""
#	g = gcf(n,d)
#	def select(name):
#		if name == 'n':
#			return n//g
#		elif name == 'd':
#			return d//g
#	return select
#	
#
#def numer(x):
#	"""Returns numerator of a rational number x."""
#	return x('n')
#
#def denom(x):
#	"""Returns denominator of rational number x."""
#	return x('d')

#===============================================================

#Necessary extra part

def gcf(a,b):
	"""Returns greatest common factor of two rationals
	>>> gcf(24,12)
	12
	>>> gcf(12, 5)
	1
	>>> gcf(81, 30)
	3
	>>> gcf(121, 22)
	11
	>>> gcf(42, 146)
	2
	"""
	if a <= 0:
		return 1
	if b <= 0:
		return 1
	if a < b:
		return gcf(b,a)
	elif a == b:
		return a
	else:
		return gcf(a-b, b)


