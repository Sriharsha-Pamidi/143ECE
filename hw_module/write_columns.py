def write_columns(data,fname):
	'this function writes formula data_value, data_value**2, (data_value+data_value**2)/3 to three columns to a comma-separated file'
	assert type(data) == list
	assert type(fname) == str

	for datum in data:
		assert type(datum) == int or type(datum) == float

	with open(fname,'a') as f:
		for datum in data: 
			f.write("{0:.2f}, {1:.2f}, {2:.2f}\n".format(datum, datum**2, (datum+datum**2)/3))
