from operator import *
"""tree = [x for x in range(5)]
for a in tree:

	for b in range(a-1):
		print(a, " ", end="")

	print(a)
"""


"""fib = [1, 1]
for x in range(9):
	fib.append(  add( fib[len(fib)-2], fib[len(fib)-1] )  )

for x in fib:
	for y in range(x-1):
		print("1 ", end = "")
	print(x)

area = 20
heights = [x for x in range(area)]
min([x for perim in ])"""

nums = [x for x in range(25)]
for x in nums:
	print(x)

squares = [x*x for x in nums if x < 20]

for x in squares:
	print(x)
