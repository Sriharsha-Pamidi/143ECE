def next_permutation(nums_tu):
	'''Given a permutation of any length, generate the next permutation in lexicographic order. F
	or example, this are the permutations for [1,2,3] in lexicographic order.'''
	assert type(nums_tu) == tuple
	assert len(nums_tu) > 1
	assert len(nums_tu) == len(set(nums_tu))
	for i in nums_tu:
		assert nums_tu[i] >= 0

	nums = list(nums_tu)
	found = False
	i = len(nums) - 2
	while i >= 0:
		if nums[i] < nums[i + 1]:
			found = True
			break
		i -= 1
	if not found:
		nums.sort()
	else:
		m = findMaxIndex(i + 1, nums, nums[i])
		nums[i], nums[m] = nums[m], nums[i]
		nums[i + 1:] = nums[i + 1:][::-1]
	return tuple(nums)


def findMaxIndex(index, a, curr):
	ans = -1
	index = 0
	for i in range(index, len(a)):
		if a[i] > curr:
			if ans == -1:
				ans = curr
				index = i
			else:
				ans = min(ans, a[i])
				index = i
	return index
