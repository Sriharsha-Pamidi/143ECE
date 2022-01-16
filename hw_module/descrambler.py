import itertools


def descrambler(input_word_string, k_tuple):
	'''You are given a sequence of n lower-case letters and a k-tuple of integers that indicate partition-lengths
	of the sequence. Also, you have a dictionary of commonly used words. The n letters represent a phrase of k words
	where the length of the j t h word is the j t h element of the tuple.'''

	assert type(input_word_string) == str
	assert type(k_tuple) == tuple
	assert sum(k_tuple) == len(input_word_string)
	for i in k_tuple:
		assert i >= 0
	assert len(input_word_string) > 0

	from collections import defaultdict
	word_dict = defaultdict(list)
	with open("google-10000-english-no-swears.txt") as f:
		for line in f:
			line = line.replace("\n", "")
			if all(c_in_string(line, input_word_string)):
				key = "".join(sorted(line))
				word_dict[key].append(line)

	pois = stem_combinations(word_dict,input_word_string,k_tuple)
	valid_sequences = []
	for poi in pois:
		valid_sequence = []
		while len(poi[1]) > 0:
			valid_sequence.append(poi[0])
			poi = poi[1][0]
		valid_sequences.append(valid_sequence)

	for seq in valid_sequences:
		word_sequences = []
		for i in range(len(seq)):
			word_sequences.append(word_dict[seq[i]])
		for element in itertools.product(*word_sequences):
			yield ' '.join(element)


def stem_combinations(word_dict, word_string, k_tuple):
	combination = []
	if len(k_tuple) > 0:
		p_words = get_combination(word_dict, word_string, k_tuple[0])
		for p_word in p_words:
			sc = stem_combinations(word_dict,str_remove(word_string,p_word),k_tuple[1:])
			if len(sc) > 0:
				combination.append((p_word,sc))
	else:
		combination.append((word_string,[]))
	return combination


def get_combination(word_dict, w_string, word_len):
	combs = itertools.combinations(w_string, word_len)
	valid_possibs = set()
	for word in combs:
		stem = ''.join(sorted(word))
		if stem in word_dict:
			valid_possibs.add(stem)
	return valid_possibs


def str_remove(word_string, p_word):
	for ch in p_word:
		word_string = word_string.replace(ch,"",1)
	return word_string

def c_in_string(line,istring):
	for c in line:
		yield c in istring