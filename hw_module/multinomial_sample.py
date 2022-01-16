def factorial(n):
	from functools import reduce
	if n == 0:
		return 1
	return reduce(lambda x, y: x * y, range(1, n + 1))


def multinomial_sample(n, p, k=1):
	'''
	Return samples from a multinomial distribution.

	n:= number of trials
	p:= list of probabilities
	k:= number of desired samples
	'''

	assert type(n) == int and type(p) == list and type(k) == int
	assert k > 0 and len(p) > 0 and n > 0
	assert sum(p) == 1

	from itertools import product
	from math import pow
	import random

	sample_space = [x for x in product(list(range(n + 1)), repeat=len(p)) if sum(x) == n]
	n_fact = factorial(n)

	sample_prob = []
	for sample in sample_space:
		c = n_fact
		for ind,val in enumerate(sample):
			c = c * (pow(p[ind], val) / factorial(val))
		sample_prob.append(c)

	return [list(k) for k in random.choices(sample_space, sample_prob, k=k)]
