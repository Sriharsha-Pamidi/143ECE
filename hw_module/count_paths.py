def count_paths(m,n,blocks):
	'''Grid Path Searching-- Here is the function signature: count_paths(m,n,blocks) where m is the number of rows
	and n is the number of columns. The blocks variable is a list of tuples indicating the blocked # entries in the
	grid.'''

	assert type(m) == int and type(n) == int
	assert type(blocks) == list

	if (0,0) in blocks:
		return 0
	# Dynamic Programming
	count_path = [[0 for _ in range(n)] for _ in range(m)]
	count_path[0][0] = 1

	for i in range(1, m):
		count_path[i][0] = int((i,0) not in blocks and count_path[i - 1][0] == 1)

	for j in range(1, n):
		count_path[0][j] = int((0,j) not in blocks and count_path[0][j - 1] == 1)

	for i in range(1, m):
		for j in range(1, n):
			if (i,j) not in blocks:
				count_path[i][j] = count_path[i - 1][j] + count_path[i][j - 1]
			else:
				count_path[i][j] = 0

	return count_path[m - 1][n - 1]
