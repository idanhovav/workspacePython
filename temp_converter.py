def temperature_converter(f_temp):
	""" A function that returns the celsius temperature
	of a fahrenheit temperature it's passed
    >>> celsius_temp1 = temperature_converter(32)
    >>> celsius_temp1
    0.0
    """
	c_temp = f_temp - 32
	c_temp = c_temp * 5
	c_temp = c_temp / 9

	return c_temp