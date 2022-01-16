def threshold_values(seq,threshold=1):
	''' From gather_values, we can group the results of the random samples. Now, we want to threshold those values based
	upon their frequency and value. Given threshold=2, we want to keep only those bitstrings with the two highest
	frequency counts of the 1 value'''

	assert type(seq) == list
	assert type(threshold) == int and threshold > 0
	from collections import defaultdict

	gather_dict = defaultdict(list)
	for bits in seq:
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
	assert sample_count == len(seq)

	# If there is a tie, then use the smallest value the tied bitstrings to pick the winner
	sorted_gather_dct = sorted(gather_dict.items(), key=lambda i: int(i[0],2))
	sorted_gather_dict = sorted(dict(sorted_gather_dct).items(), key=lambda i: len(i[1]), reverse=True)
	threshold_count = 0
	threshold_dict = defaultdict(int)
	for key in dict(sorted_gather_dict).keys():
		if threshold_count < threshold and gather_dict[key][0] == 1:
			threshold_dict[key] = 1
			threshold_count += 1
		else:
			threshold_dict[key] = 0

	return threshold_dict
