def gather_values(sample_list):
	''' Now that you have get_sample working, generate n samples and tally the number of times an existing key is repeated.
	Generate a new dictionary with bitstrings as keys and with values as lists that contain the corresponding mapped
	values from map_bitstring. Here is an example for n=20,
	Write a function gather_values that can produce the following output from x:
	x=get_sample(nbits=2,prob={'00':1/4,'01':1/4,'10':1/4,'11':1/4},n=20)
	{'10': [1, 1, 1, 1, 1],
	'11': [1, 1, 1, 1, 1, 1],
	'01': [1, 1, 1],
	'00': [0, 0, 0, 0, 0, 0]}'''
	assert type(sample_list) == list
	from collections import defaultdict

	gather_dict = defaultdict(list)
	for bits in sample_list:
		count_0 = 0
		for i in range(len(bits)):
			if bits[i] == '0':
				count_0 += 1
		if count_0 > (len(bits) - count_0):
			gather_dict[bits].append(0)
		else:
			gather_dict[bits].append(1)
		assert bits in gather_dict

	sample_count = 0
	for count_list in gather_dict.values():
		sample_count += len(count_list)
	assert sample_count == len(sample_list)

	return gather_dict
