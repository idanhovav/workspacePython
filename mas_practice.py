def count(s, value):
	""" A function that returns the number of times a specific
	value it's passed is present in a specific list it is passed.

	>>> count([1,2], 1)
	1
	>>> count ([2,2,2,2,2,1], 2)
	5
	>>> count([4,6,7,4,12,4,6,8,4,4,4], 4)
	6

	"""
	total, index = 0,0

	while index < len(s):
		if s[index] == value:
			total = total + 1
		index = index + 1

	return total

def count_for_loop(s, value):
	total = 0
	for elem in s:
		if elem == value:
			total = total + 1

	return total