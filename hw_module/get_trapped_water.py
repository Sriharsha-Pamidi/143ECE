def get_trapped_water(seq):
	'''You are given an array of non-negative integers that represents a two-dimensional elevation map where each
	element is unit-width wall and the integer value is the height. Suppose rain fills all available gaps between
	two bordering walls. Compute how many units of water remain trapped between the walls in the map.
	'''
	assert type(seq) == list
	assert len(seq) > 2

	left = 0
	right = len(seq) - 1

	# To store Left max and right max
	# for two pointers left and right
	l_max = 0
	r_max = 0

	result = 0
	while left <= right:
		if r_max <= l_max:
			result += max(0, r_max - seq[right])
			r_max = max(r_max, seq[right])
			right -= 1
		else:
			result += max(0, l_max - seq[left])
			l_max = max(l_max, seq[left])
			left += 1
	return result