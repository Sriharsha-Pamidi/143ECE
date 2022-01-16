def all_sublists(list_range):
	'This function generate all sublists of a list using recursion'
	assert type(list_range) == list and len(list_range) > 0 and len(list_range) == len(set(list_range))

	if len(list_range) == 1:
		return [list_range]

	elem_list_range = list_range[0]
	sub_list_range = list_range[1:]

	complete_sublists = all_sublists(sub_list_range) + [[elem_list_range]] + [[elem_list_range]+sub for sub in all_sublists(sub_list_range)]
	assert len(complete_sublists) == 2**len(list_range)-1
	return complete_sublists
