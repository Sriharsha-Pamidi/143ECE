def map_bitstring(bitstring_list):
	'''this function takes a list of bitstrings and maps each bitstring to 0 if the number of 0s in the bitstring
	strictly exceeds the number of 1s. Otherwise, map that bitstring to 1'''
	assert type(bitstring_list) == list

	bitstring_dict = {}
	for bits in bitstring_list:
		count_0 = 0
		for i in range(len(bits)):
			if bits[i] == '0':
				count_0 += 1

		if count_0 > (len(bits)-count_0):
			bitstring_dict[bits] = 0
		else:
			bitstring_dict[bits] = 1
		assert bits in bitstring_dict

	return bitstring_dict
