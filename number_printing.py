def split(n):
	return n // 10, n % 10

def print_down(n):
	""" Prints a number repeatedly taking away last digit until end.
	>>> print_down(2015)
	2015
	201
	20
	2
	Done.

	"""
	print(n)
	rest_of_num, last_num = split(n)
	if rest_of_num == 0:
		print("Done.")
	else: 
		print_down(rest_of_num)

def print_up(n):
	""" Prints a number up repeatedly adding the last digit until the original number.
	>>> print_up(2015)
	2
	20
	201
	2015
	"""
	rest_of_num, last_num = split(n)
	if rest_of_num != 0:
		print_up(rest_of_num)
	print(n)





