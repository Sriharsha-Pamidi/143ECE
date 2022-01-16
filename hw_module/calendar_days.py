def number_of_days(year,month):
	'this function returns the number of calendar days in a given year and month'
	assert isinstance(year,int) and isinstance(month,int) and year>0 and month>=1 and month<=12 
	from calendar import monthrange
	return monthrange(year, month)[1]

def number_of_leap_years(year1,year2):
	'this function to find the number of leap-years between (including both endpoints) two given years'
	assert isinstance(year1,int) and isinstance(year2,int) and year2>=year1 and year2>0 and year1>0

	from calendar import isleap
	count = 0
	for year in range(year1,year2+1):
		if isleap(year):
			count += 1 
	return count

def get_day_of_week(year,month,day):
	'this function to find the string name of the day of the week on a given month,day and year'
	assert year>0 and month>=1 and month<=12 and day>=1 and day<=31
	assert number_of_days(year,month) >= day

	from calendar import day_name,weekday
	return day_name[weekday(year,month,day)]
