def split(n):
  """A function that splits a number into it's last digit and remaining digits
  >>> split(2016)
  (201, 6)
  >>> split (5)
  (0, 5)
  >>> split(48)
  (4, 8)
  """
  rest_of_num, last_num = n // 10, n % 10
  return rest_of_num, last_num

def luhn_sum(n):
  """ A function that finds the luhn sum of a number it's given. Luhn sum
  is defined as the sum of all the digits of a number, with every second
  digit being doubled. If the double of that digit is > 10, then the sum of
  the digits of that number is returned.

  >>> luhn_sum(2015)
  11
  >>> luhn_sum(28)
  12
  >>> luhn_sum(11111)
  7
  >>> luhn_sum(4354366)
  35
  >>> luhn_sum(12345)
  21
  """
  rest_of_num, last_num = split(n)

  if rest_of_num == 0:
  	return last_num
  else:
  	return last_num + luhn_double_sum(rest_of_num)


def luhn_double_sum(n):
  """ The second part of the luhn sum function, which doubles the 
  second number, and recurses between itself and luhn sum.
  """
  rest_of_num, last_num = split(n)

  doubled_last_num = last_num*2
  if (doubled_last_num) >= 10:
  	doubled_last_num = sum_of_digits(doubled_last_num)
  if rest_of_num == 0:
  	return doubled_last_num
  return doubled_last_num + luhn_sum(rest_of_num)


def sum_of_digits(n):
  """ A function that uses recursion to add up the sum of the digits of a number.
  The function splits the number into the last number and the rest of the numbers
  in each recursion, and then adds up the digits once it gets to the last digit.
  >>> sum_of_digits(18)
  9
  >>> sum_of_digits(32355)
  18
  >>> sum_of_digits(4365767)
  38
  """
  rest_of_num, last_num = split(n)
  if rest_of_num < 10:
  	return last_num + rest_of_num
  return last_num + sum_of_digits(rest_of_num)


