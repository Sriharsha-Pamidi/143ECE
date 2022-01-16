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


def count_month_yr(x):
	'''Your function add_month_yr(x) should take in the x survey dataframe
	and then output the same dataframe with a new month-yr column'''
	assert type(x) == pd.DataFrame
	assert 'month-yr' in x.columns
	month_series = x['month-yr'].value_counts()
	month_frame = month_series.to_frame()
	month_frame.rename(columns = {'month-yr':'Timestamp'}, inplace=True)
	month_frame.index.name = 'month-yr'
	return month_frame
