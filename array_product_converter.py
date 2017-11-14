def array_product_converter(nums):
	length = len(nums)
	temps = []

	for x in range(0, length):
		temps.append(nums[x])


	for x in range (0, length):

		print("Temps: ", temps)
		product = 1

		for y in range(0, length):
			if (not x == y):
				product *= temps[y]
				print("Temps 2: ", temps)

		#print(product)

		nums[x] = product
		print("Temps 3: ", temps)

	print(nums)

def array_product_converter2(nums):

	product = 1
	zerocounter = 0

	for x in nums:
		if (x == 0):
			zerocounter = zerocounter + 1


	if(zerocounter > 1):
		return makeAllZero(nums)
	if(zerocounter == 1):
		return specialCaseZero(nums)

	for x in nums:
		product = product * x

	for x in range (0, len(nums)):
		nums[x] = product / (nums[x])

	return nums

def makeAllZero(nums):
	for x in range(0, len(nums)):
		nums[x] = 0

	return nums

def specialCaseZero(nums):
	zeroelem = 0
	product = 1

	for x in range (0, len(nums)):
		if(nums[x] == 0):
			zeroelem = x

	for x in range(0, len(nums)):
		if(not x == zeroelem):
			product = product * nums[x]
	nums = makeAllZero(nums)

	nums[zeroelem] = product

	return nums






