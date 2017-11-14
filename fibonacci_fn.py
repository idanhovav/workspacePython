def fibonacci_num(element):
	""" Calculate the element in the fibonacci sequence given.
	The function employs recursion in its final line, and it's
	base cases are if the element is asking for the 1st term, or
	the 2nd term of the sequence.

	>>> fibonacci_num(1)
	1
	>>> fibonacci_num(2)
	1
	>>> fibonacci_num(4)
	3
	>>> fibonacci_num(8)
	21

	"""
	if element < 1:
		print("Invalid input. Process cancelled")
	elif element == 1:
		return 1
	elif element == 2:
		return 1
	else:
		return fibonacci_num(element - 1) + fibonacci_num(element - 2)