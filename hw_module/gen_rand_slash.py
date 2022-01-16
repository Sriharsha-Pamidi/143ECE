def gen_rand_slash(m=6, n=6, direction='back'):
	'''The function produces a uniformly random forward or backslashed image (i.e., Numpy array)
	of at least two non-zero pixels'''

	import numpy as np
	import random

	assert type(m) == int and m > 1 and type(n) == int and n > 1 and type(direction) == str
	assert direction == 'forward' or direction == 'back'

	x_arr = np.zeros([m, n])
	k = random.choice(range(2, min(m, n) + 1))

	if direction == 'forward':
		r_r = random.choice(range(m - k + 1))
		r_c = random.choice(range(k - 1, n))
		for i in range(k):
			x_arr[r_r][r_c] = 1
			r_r = r_r + 1
			r_c = r_c - 1
		return x_arr

	if direction == 'back':
		r_r = random.choice(range(m - k + 1))
		r_c = random.choice(range(n - k + 1))
		for i in range(k):
			x_arr[r_r][r_c] = 1
			r_r = r_r + 1
			r_c = r_c + 1
		return x_arr
