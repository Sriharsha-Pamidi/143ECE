def get_average_word_length(words):
	'''Compute the average length of the words'''
	assert type(words) == list
	assert len(words) > 0
	for word in words:
		assert type(word) == str

	length = [len(word) for word in words]
	return sum(length) / len(length)


def get_longest_word(words):
	'''What is the longest word'''
	assert type(words) == list
	assert len(words) > 0
	for word in words:
		assert type(word) == str

	word_length = [(word, len(word)) for word in words]
	sorted_word_length = sorted(word_length, key=lambda i: i[1], reverse=True)
	return sorted_word_length[0][0]


def get_longest_words_startswith(words, start):
	'''What is the longest word that starts with a single letter'''
	assert type(words) == list
	assert len(words) > 0
	assert type(start) == str
	for word in words:
		assert type(word) == str

	words_start_length = [(word, len(word)) for word in words if word[0] == start]
	sorted_words_start_length = sorted(words_start_length, key=lambda i: i[1], reverse=True)
	return sorted_words_start_length[0][0]


def get_most_common_start(words):
	'''What is the most common starting letter '''
	assert type(words) == list
	assert len(words) > 0
	for word in words:
		assert type(word) == str

	from collections import defaultdict
	letter_dict = defaultdict(int)
	for word in words:
		letter_dict[word[0]] += 1
	sorted_letter_dict = sorted(letter_dict, key=lambda i: letter_dict[i], reverse=True)
	return sorted_letter_dict[0]


def get_most_common_end(words):
	'''What is the most common ending letter'''
	assert type(words) == list
	assert len(words) > 0
	for word in words:
		assert type(word) == str

	from collections import defaultdict
	letter_dict = defaultdict(int)
	for word in words:
		letter_dict[word[-1]] += 1
	sorted_letter_dict = sorted(letter_dict, key=lambda i: letter_dict[i], reverse=True)
	return sorted_letter_dict[0]
