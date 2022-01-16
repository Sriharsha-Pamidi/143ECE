import numpy as np


def find_convex_cover(pvertices, clist):
	'''Given a irregular, closed, convex polygon P with n−1 sides and m circle-centers contained within that polygon,
	compute the radii of m circles centered at those m points such that the sum of the areas of the circles is
	minimized (approximately) and that any vertex in P is also contained in at least one of the m circles.'''

	assert type(pvertices) == np.ndarray and len(pvertices) > 2
	assert type(clist) == list and len(clist) > 0

	centers = np.array(clist)
	distances = np.linalg.norm(pvertices[:, np.newaxis, :] - centers, axis=2)
	distances = np.hstack((np.zeros((pvertices.shape[0], 1)), distances))

	print("vert", pvertices.shape)
	print("center", centers.shape)
	print("dis", distances.shape)



	iters = 0
	for i in range(pvertices.shape[0]):
		m_shape = []
		for j in range(pvertices.shape[0]+1):
			if j == i:
				print(distances[i])
				m_shape.append(len(distances[i]))
			else:
				m_shape.append(1)
		iters = np.broadcast(iters, distances[i].reshape(tuple(m_shape)))

	iters_list = list(iters)
	iter_list = [it[1:] for it in iters_list]
	sorted_iters = sorted(iter_list, key=lambda itk: sum(map(lambda x: x * x, itk)))
	for it in sorted_iters:
		if valid_vertex_circles(pvertices, centers, it):
			return list(it)
	print(sorted_iters)
	assert False


def valid_vertex_circles(pvertices, centers, rads):
	result = [False] * len(pvertices)
	for ic, center in enumerate(centers):
		for iv, vertex in enumerate(pvertices):
			if not result[iv]:
				print(vertex,center,rads,ic)
				if point_in_circle(vertex, center, rads[ic]):
					result[iv] = True
	return all(result)


def point_in_circle(point, center, rad):
	(x, y) = point
	(circle_x, circle_y) = center
	if (x - circle_x) * (x - circle_x) + (y - circle_y) * (y - circle_y) <= rad * rad:
		return True
	else:
		return False
