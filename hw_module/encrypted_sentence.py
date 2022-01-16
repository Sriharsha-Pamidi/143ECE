def encrypt_message(message, fname):
	'''
	Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
	name of a text file source for the codebook, generate a sequence of 2-tuples that
	represents the `(line number, word number)` of each word in the message. The output is a list
	of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.

	:param message: message to encrypt
	:type message: str
	:param fname: filename for source text
	:type fname: str
	:returns: list of 2-tuples
	'''

	assert type(message) == str and type(fname) == str
	import string, random
	from collections import defaultdict

	cipher_dict = defaultdict(list)
	line_count = 0
	with open(fname) as f:
		for line in f:
			line_count = line_count + 1
			line = ''.join(ch for ch in line.lower() if ch not in string.punctuation)
			for index, word in enumerate(line.split()):
				cipher_dict[word] += [(line_count, index + 1)]

	message_dict = defaultdict(list)
	for index,word in enumerate(message.split()):
		message_dict[word].append(index)

	encrypted_message = message.split()
	for word in message_dict.keys():
		count = len(message_dict[word])
		assert len(cipher_dict[word]) >= count
		sampled_ciphers = random.sample(cipher_dict[word],count)
		for k,cipher in zip(message_dict[word],sampled_ciphers):
			encrypted_message[k] = cipher

	assert len(encrypted_message) == len(set(encrypted_message))
	return encrypted_message


def decrypt_message(inlist, fname):
	'''
	Given `inlist`, which is a list of 2-tuples`fname` which is the
	name of a text file source for the codebook, return the encrypted message.

	:param message: inlist to decrypt
	:type message: list
	:param fname: filename for source text
	:type fname: str
	:returns: string decrypted message
	'''

	assert type(inlist) == list and type(fname) == str
	import string

	lines = []
	with open(fname) as f:
		for line in f:
			lines.append(''.join(ch for ch in line.lower() if ch not in string.punctuation))

	decrypt_words = []
	for line, index in inlist:
		decrypt_words.append(lines[line - 1].split()[index - 1])
	return ' '.join(decrypt_words)
