def fibonacci(n):
	'This function returns a generator to compute the first n Fibonacci numbers'
	assert type(n) == int

	f_list = []
	if n > 0:
		f_list.append(1)
	if n > 1: 
		f_list.append(1)
	for i in range(1,n-1):
		f_list.append(f_list[i] + f_list[i-1])
	assert len(f_list) == n

	for f_num in f_list:
		yield f_num
