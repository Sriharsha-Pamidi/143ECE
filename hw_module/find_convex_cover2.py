from collections import defaultdict

import numpy as np


def find_convex_cover(pvertices, clist):
	'''Given a irregular, closed, convex polygon P with n−1 sides and m circle-centers contained within that polygon,
	compute the radii of m circles centered at those m points such that the sum of the areas of the circles is
	minimized (approximately) and that any vertex in P is also contained in at least one of the m circles.'''

	assert type(pvertices) == np.ndarray and len(pvertices) > 2
	assert type(clist) == list and len(clist) > 0

	centers = np.array(clist)
	distances = np.linalg.norm(pvertices[:, np.newaxis, :] - centers, axis=2)

	min_dict = defaultdict(tuple)
	for i in range(len(distances)):
		min_dict[tuple(pvertices[i])] = (clist[np.argmin(distances[i])],np.min(distances[i]))

	min_rad = defaultdict(float)
	for tup,dis in min_dict.values():
		min_rad[tup] = max(min_rad[tup],dis)

	return [min_rad[item] for item in clist]
