def split(n):
	"""Returns the last digit of a number. 
	And the first digit of a number. 
	Does not have any other impacts
	
	>>> split(2015)
	(201, 5)
	>>> split(76)
	(7, 6)
	"""
	rest_of_num, last_num = n // 10, n % 10
	return rest_of_num, last_num

