import calendar
import pandas as pd


def add_month_yr(x):
	'''Your function add_month_yr(x) should take in the x survey dataframe
	and then output the same dataframe with a new month-yr column'''
	assert type(x) == pd.DataFrame
	timestamps = x['Timestamp']
	assert len(timestamps) > 0
	time_split = timestamps.str.split('/+| ',expand=True)
	time_split['month-yr'] = time_split.apply(lambda d: calendar.month_abbr[int(d[0])] + '-' + d[2], axis=1)
	x['month-yr'] = time_split['month-yr']
	return x
