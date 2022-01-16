def write_chunks_of_five(words,fname):
	'creates a new file that consists of each consecutive non-overlapping sequence of five lines merged into one line'
	assert type(words) == list
	assert type(fname) == str

	for word in words:
		assert type(word) == str

	i = 0
	with open(fname,'a') as f:
		while(i + 5 < len(words)):
			f.write(' '.join(words[i:i+5])+"\n")

			i = i + 5
		f.write(' '.join(words[i:len(words)])+"\n")
