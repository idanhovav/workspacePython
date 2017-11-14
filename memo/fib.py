def fib(n):
	#naive recursion
	if n == 0 or n == 1:
		return 1
	return fib(n-1)+fib(n-2)

def memofib(n, d={0:1, 1:1}):
	#memoization
	if n not in d:
		d[n] = memofib(n-1, d) + memofib(n-2, d)
	return d[n]

	# greedy programming
def change(total, coins, used):
	# candidate set: coins

	#solution function
	if total == 0:
		return used
	# selection function: biggest coin
	# feasibility function: if <= total
	elif coins[0] <= total:
		used += [coins[0]]
		return change(total-coins[0], coins, used)
	else:
		return change(total, coins[1:], used)
	# implicit objective function: use least amount of coins 