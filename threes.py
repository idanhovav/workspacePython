#
# A program inspired by https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/
#

import time

def threes_path_recursive(num):
	if num == 1:
		print(num)
		return
	change = num_to_change(num)
	print(num, change)
	return threes_path_recursive((num + change) // 3)

def threes_path_loop(num):
	change = 0
	while num != 1:
		change = num_to_change(num)
		print(num, change)
		num = (num + change) // 3
	print(num)
	return

def num_to_change(n):
	n_remainder_three = n % 3
	return (n_remainder_three // 2) - (n_remainder_three % 2)

def measure_fn_speed(fn, inp):
	startTime = time.clock()
	fn(inp)
	endTime = time.clock()
	print(endTime - startTime)

measure_fn_speed(threes_path_recursive, 31337378572)

measure_fn_speed(threes_path_loop, 31337378572)