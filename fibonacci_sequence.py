def fibonacci_sequence(x):
	"""Given element position in fibonacci sequence, returns value.

	>>> fibonacci_sequence(0)
	0
	>>> fibonacci_sequence(3)
	2
	>>> fibonacci_sequence(12)
	144
	"""
	
	if(x == 0):
		return 0;
	if(x == 1):
		return 1;
	else:
		return fibonacci_sequence(x-1) + fibonacci_sequence(x-2)
