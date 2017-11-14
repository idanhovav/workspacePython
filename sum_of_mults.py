def sum_of_mults(a, b, lim):
	"""A function that adds up the integers divisible
	by integers a and b up to a number lim

    >>> sum_of_mults(3, 5, 10)
    23
    >>> sum_of_mults(3, 7, 1000)
    214216
    >>> sum_of_mults(2, 5, 22)
    130
    >>> sum_of_mults(3, 7, 29)
    184
    >>> sum_of_mults(12, 11, 2222)
	411819
	"""
	total = 0

	for x in range(lim):

		if x % a == 0 or x % b == 0:
			total = total + x

	return total