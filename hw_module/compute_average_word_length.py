def compute_average_word_length(instring,unique = False):
	'This function computes the average length of the words in the input string. If the unique option is True, then excludes duplicated words'
	assert type(instring) == str
	assert type(unique) == bool

	if unique == True:
		words = list({word.lower() for word in instring.split()})
	else:
		words = [word.lower() for word in instring.split()]

	word_lengths = [len(word) for word in words]
	assert len(words) > 0
	return sum(word_lengths)/len(words)
