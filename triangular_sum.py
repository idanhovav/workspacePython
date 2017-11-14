def triangular_sum(n):
	""" A function that finds the sum of all triangle numbers
	until the nth element of the triangular number set. It also
	prints those triangle numbers.

	n >= 1

	>>> t_sum = triangular_sum(5)
	1
	3
	6
	10
	15
	>>> t_sum
	35

	"""
	triangle_nums = []
	x = 1
	total = 0
	while x <= n:
		triangle_nums = triangle_nums + [triangle_num(x)]
		x = x + 1

	for elem in triangle_nums:
		print(elem)
		total = total + elem
	return total


#===================================================================
#Abstraction barrier waddup


def triangle_num(n):
	"""Calculates the triangle number in the set of triangle numbers
	based on the element n in the set it is passed.

	>>> triangle_num(1)
	1
	>>> triangle_num(2)
	3
	>>> triangle_num(5)
	15

	"""

	if n == 1:
		return n

	else:
		return n + triangle_num(n-1)



