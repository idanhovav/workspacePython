import math

def find_primes(n):
	""" A function that finds and prints all the primes between 2 and
	the number n passed into it.

	n > 2

	>>> find_primes(3)
	[2, 3]
	[2, 3]

	>>> find_primes(8)
	[2, 3]
	[2, 3, 5]
	[2, 3, 5, 7]
	[2, 3, 5, 7]

	>>> find_primes(19)
	[2, 3]
	[2, 3, 5]
	[2, 3, 5, 7]
	[2, 3, 5, 7, 11]
	[2, 3, 5, 7, 11, 13]
	[2, 3, 5, 7, 11, 13, 17]
	[2, 3, 5, 7, 11, 13, 17, 19]
	[2, 3, 5, 7, 11, 13, 17, 19]

	"""

	#Primes found already. Starts with 2 cuz fuck u
	primes = [2]
	#Numbers being checked for primity.
	# Starts with 3 b/c we started primes at 2
	num = 3

	while num <= n:

		if is_prime(num, primes):
			primes = primes + [num]
			#Obvious reason for print statement is obvious
			#print(primes)

		#Print statements to check if working
		#print("Checker: ", checker)
		#print("Number Checked: ", num)
		
		num = num + 1 

	return primes


def is_prime(num, primes):
	""" Returns boolean value of whether a specific number is prime
	or not. User beware: list passed in for second argument must have
	all primes up to the number passed in or the function will not 
	work.

	>>> is_prime(3, [2])
	True

	>>> is_prime(5, [2,3])
	True

	>>> is_prime(8, [2,3,5])
	False

	"""
	for elem in primes:

		if num % elem == 0:
			return False

	return True

def better_is_prime(a):
	"""
	>>> better_is_prime(4)
	False
	>>> better_is_prime(5)
	True
	>>> better_is_prime(6)
	False
	>>> better_is_prime(7)
	True
	>>> better_is_prime(8)
	False
	>>> better_is_prime(9)
	False
	>>> better_is_prime(10)
	False
	>>> better_is_prime(11)
	True
	>>> better_is_prime(12)
	False
	>>> better_is_prime(13)
	True
	>>> better_is_prime(14)
	False
	"""
	b = 2
	while b <= math.sqrt(a):
		if a % b == 0:
			return False
		b += 1
	return True
