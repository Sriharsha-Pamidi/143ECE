def is_string_integer(s):
	'this function that a single string character as input and returns if that character represents a valid integer in base 10'
	assert type(s) == str
	assert len(s) == 1
	if s.isdigit() != True:
		return False
	return True
