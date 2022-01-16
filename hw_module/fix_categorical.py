import calendar
import pandas as pd


def add_month_yr(x):
	'''Your function add_month_yr(x) should take in the x survey dataframe
	and then output the same dataframe with a new month-yr column'''
	assert type(x) == pd.DataFrame
	timestamps = x['Timestamp']
	assert len(timestamps) > 0
	time_split = timestamps.str.split('/+| ', expand=True)
	time_split['month-yr'] = time_split.apply(lambda d: calendar.month_abbr[int(d[0])] + '-' + d[2], axis=1)
	x['month-yr'] = time_split['month-yr']
	return x


def fix_categorical(x):
	'''Convert the month-yr column dtype to a Pandas CategoricalDtype with the correct order
	It should take the month-yr dataframe column and then return the same dataframe with an updated column of
	CategoricalDtype that does the sorting as described.
	x is a pd.DataFrame with the required "month-yr" column and output is a pd.DataFrame with the "month-yr"
	column having the categorical dtype.
	'''
	assert type(x) == pd.DataFrame
	assert 'month-yr' in x.columns

	categories = x['month-yr'].unique()
	cat_type = pd.api.types.CategoricalDtype(categories=categories, ordered=True)
	x['month-yr'] = x['month-yr'].astype(cat_type)
	return x
