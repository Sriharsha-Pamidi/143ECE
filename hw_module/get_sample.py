def get_sample(nbits=3, prob=None, n=1):
	'''Given a number of bits, the get_sample function returns a list n of random samples from a finite
	probability mass function defined by a dictionary with keys defined by a specified number of bits'''

	from random import choices
	assert type(prob) == dict
	assert type(n) == int
	assert type(nbits) == int
	assert n > 0
	assert nbits > 0
	assert len(prob) > 0

	total = 0
	for v in prob.values():
		total += v
		assert type(v) == int or type(v) == float
	assert total == 1

	samples = []
	probabs = []
	for key, value in prob.items():
		assert type(key) == str
		assert len(key) == nbits
		samples.append(key)
		probabs.append(value)
	return choices(samples, probabs, k=n)
