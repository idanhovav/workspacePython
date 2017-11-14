# Created by Idan Hovav, 24 May 2015
# Stay ballin San Francisco



#GLOBAL FORMAT FOR BINARY HAS A O TO START WITH. ALWAYS MUDDAFUCKA

#TODO: 
#- Make binary adder wth ints passed into function
#- Create converter from binary to int
#- Figure out how to fucking multiply goddam
#-be happy

#Converts a number passed into it into binary
#only works for 0 < a < 1048576
def converter_to_bin(num):
	""" To find what 2 exponents a number is made of, use subtraction.
	If a 2-exp can be taken out, then it is present, and that is marked
	in the list that represents the binary number.

	>>> converter_to_bin(0)
	[0]

	>>> converter_to_bin(1)
	[0, 1]

	>>> converter_to_bin(2)
	[0, 1, 0]

	>>> converter_to_bin(3)
	[0, 1, 1]

	>>> converter_to_bin(4)
	[0, 1, 0, 0]

	>>> converter_to_bin(9)
	[0, 1, 0, 0, 1]

	>>> converter_to_bin(11)
	[0, 1, 0, 1, 1]

	>>> converter_to_bin(16)
	[0, 1, 0, 0, 0, 0]

	>>> converter_to_bin(14)
	[0, 1, 1, 1, 0]

	>>> converter_to_bin(22)
	[0, 1, 0, 1, 1, 0]

	>>> converter_to_bin(31)
	[0, 1, 1, 1, 1, 1]
	"""

	binary = [0]

	#How many bits are needed?
	#print statements are checkers
	for x in range (0, 20):
		#print('a')
		if (num < pow(2, x)):
			#print(x)
			for counter in range (0, x):
				#print('b')
				binary.append(0)
			break

	#print(binary)


	#rest of code is based on number of bits  of the number
	length = len(binary)

	for x in range(0, length):

		if(num - pow(2, (length-1)-x) >= 0 and (not (num == 0))):
			num = num - pow(2, (length-1)-x)
			binary[x] = binary[x] + 1

	return binary

def same_num_of_bits_ints(a, b):
	""" Adds zeroes in the front of the binary representation
	of integers a and b to make them have the same number of bits.
	Returns binary representation of integers with same number of 
	bits.

	>>> A, B = same_num_of_bits_ints(1, 5)
	>>> A
	[0, 0, 0, 1]
	>>> B
	[0, 1, 0, 1]

	>>> A, B = same_num_of_bits_ints(12, 3)
	>>> A
	[0, 1, 1, 0, 0]
	>>> B
	[0, 0, 0, 1, 1]

	>>> A, B = same_num_of_bits_ints(10, 25)
	>>> A
	[0, 0, 1, 0, 1, 0]
	>>> B
	[0, 1, 1, 0, 0, 1]

	"""
	bin_a, bin_b = converter_to_bin(a), converter_to_bin(b)

	a_bits, b_bits = len(bin_a), len(bin_b)

	while(not(a_bits == b_bits)):

		if(a_bits > b_bits):
			bin_b.insert(0, 0)

		elif (a_bits < b_bits):
			bin_a.insert(0, 0)

		a_bits, b_bits = len(bin_a), len(bin_b)

	return bin_a, bin_b

def same_num_of_bits_binary(a, b):
	""" Adds zeroes in the front of the binary numbers
	a and b to make them have the same number of bits.
	Returns binary numbers with same number of bits.

	>>> A,B = same_num_of_bits_binary( [0, 1] , [0, 1, 0, 1] )
	>>> A
	[0, 0, 0, 1]
	>>> B
	[0, 1, 0, 1]

	>>> A,B = same_num_of_bits_binary( [0, 1, 1, 0, 0] , [0, 1, 1] )
	>>> A
	[0, 1, 1, 0, 0]
	>>> B
	[0, 0, 0, 1, 1]

	>>> A,B = same_num_of_bits_binary( [1, 0, 1, 0] , [0, 1, 1, 0, 0, 1] )
	>>> A
	[0, 0, 1, 0, 1, 0]
	>>> B
	[0, 1, 1, 0, 0, 1]

	"""

	a_bits, b_bits = len(a), len(b)

	while(not(a_bits == b_bits)):

		if(a_bits > b_bits):
			b.insert(0, 0)

		elif (a_bits < b_bits):
			a.insert(0, 0)

		a_bits, b_bits = len(a), len(b)

	return a, b


def binary_adder(a, b):
	""" Adds two binary numbers together and returns their binary sum
	>>> binary_adder([0,1] , [0, 1, 1, 1])
	[0, 1, 0, 0, 0]

	>>> binary_adder( [0, 1, 0, 0, 1, 1], [0, 0, 1, 1])
	[0, 1, 0, 1, 1, 0]

	>>> binary_adder([0, 1, 0, 1, 1, 0] , [0, 1, 0, 0, 1, 1, 1])			 
 	[0, 1, 1, 1, 1, 0, 1]

	"""

	#making numbers have same number of bits
	a, b = same_num_of_bits_binary(a, b)
	length = len(a)

	#creating binary total and remainder
	total = []
	remainder = 0

	#making total have same number of bits
	for x in range (0, length):
		total.append(0)

	#checking
	if(not (len(a) == len(b) and len(a)  == len(total))):
		print("problemo")

	#binary calculations, going column by column of binary
	for x in range (length-1, -1, -1):
		if(a[x] + b[x] + remainder == 0):
			total[x] = 0
			remainder = 0

		elif(a[x] + b[x] + remainder == 1):
			total[x] = 1
			remainder = 0

		elif(a[x] + b[x] + remainder == 2):
			total[x] = 0
			remainder = 1

		elif(a[x] + b[x] + remainder == 3):
			total[x] = 1
			remainder = 1

	if(total[0] == 1):
		total.insert(0, 0)

	return total


def int_adder_to_binary(a, b):
	""" Adds two ints and returns the binary sum.

	>>> int_adder_to_binary(2, 3)
	[0, 1, 0, 1]

	>>> int_adder_to_binary(6, 8)
	[0, 1, 1, 1, 0]

	>>> int_adder_to_binary(9, 20)
	[0, 1, 1, 1, 0, 1]

	"""
	a, b = converter_to_bin(a), converter_to_bin(b)

		#making numbers have same number of bits
	a, b = same_num_of_bits_binary(a, b)
	length = len(a)

	#creating binary total and remainder
	total = []
	remainder = 0

	#making total have same number of bits
	for x in range (0, length):
		total.append(0)

	#checking
	if(not (len(a) == len(b) and len(a)  == len(total))):
		print("problemo")

	#binary calculations, going column by column of binary
	for x in range (length-1, -1, -1):
		if(a[x] + b[x] + remainder == 0):
			total[x] = 0
			remainder = 0

		elif(a[x] + b[x] + remainder == 1):
			total[x] = 1
			remainder = 0

		elif(a[x] + b[x] + remainder == 2):
			total[x] = 0
			remainder = 1

		elif(a[x] + b[x] + remainder == 3):
			total[x] = 1
			remainder = 1

	if(total[0] == 1):
		total.insert(0, 0)

	return total

def converter_to_int(bin):
	""" Converts a binary value to an integer.

	>>> converter_to_int([0, 1])
	1

	>>> converter_to_int([0, 1, 1])
	3

	>>> converter_to_int([0, 1, 1, 0])
	6

	>>> converter_to_int([0, 1, 0, 0, 1, 1, 1])
	39

	>>> converter_to_int([0, 1, 0, 0, 0, 0])
	16

	>>> converter_to_int([0, 1, 0, 1, 1, 0])
	22
	"""

	total = 0;
	length = len(bin)
	for x in range(length-1, -1, -1):
		total = total + (pow(2, (length-1) - x) * bin[x])
		#print(total)
	return total

