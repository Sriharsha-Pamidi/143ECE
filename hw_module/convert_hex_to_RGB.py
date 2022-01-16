def convert_hex_to_RGB(hex_list):
	'The function converts a list of color hex-codes to list of RGB-tuples'
	assert type(hex_list) == list
	for hex in hex_list:
		assert hex[0] == '#'
	return [(int(hex[1:3], 16),int(hex[3:5], 16),int(hex[5:7], 16)) for hex in hex_list]
