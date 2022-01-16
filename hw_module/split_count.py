import pandas as pd


def split_count(x):
	'''split_count(x) where x is a pd.Series object and it returns a pd.DataFrame object
	The problem with this column is that there are multiple comma-separated values in it.
	Please write a Python function called split_count that can take this column as input and output
	the following Pandas dataframe.
	'''
	assert type(x) == pd.Series
	split_x = x.str.split(',').apply(pd.Series)
	df_series = pd.Series([])
	for i in range(split_x.shape[1]):
		df_series = df_series.append(split_x[i], ignore_index=True)
	df = df_series.value_counts(ascending=True).to_frame()
	df.rename(columns={0: 'count'}, inplace=True)
	return df
