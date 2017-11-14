def split(n):
	return n // 10, n % 10
def sum_of_digits(n):
	"""Returns sum of the digits of a number 
	>>> sum_of_digits(2015)
	8
	"""
	if n < 10:
		return n
	else:
		rest_of_digits, last = split(n)
		return (sum_of_digits(rest_of_digits) + last

def luhn_sum(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return luhn_sum_double(all_but_last) + last
def luhn_sum_double(n):
	all_but_last, last = split(n)
	luhn_digit = sum_of_digits(last * 2)
	if n < 10:
		return luhn_digit
	else:
		return luhn_sum(all_but_last) + luhn_digit