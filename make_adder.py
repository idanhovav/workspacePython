def make_adder(a):
	def adder(b):
		return a + b
	return adder
def factorial(num):
	""" Returns the factorial of the number passed in employing recursion

	>>> factorial(1)
	1
	>>> factorial(2)
	2
	>>> factorial(3)
	6
	>>> factorial(4)
	24
	>>> factorial(5)
	120
	"""
	if num == 1 or num == 0:
		return 1
	return num * factorial(num - 1)

