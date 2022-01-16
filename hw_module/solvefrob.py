import numpy as np


def solvefrob(coefs, b):
	'''The Frobenius equation is the Diophantine equation
	a_1 x_1 +... + a_n x_n = b
	where a_i> 0 are positive integers, b> 0 is a positive integer, and the solution x_i consists of non-negative integers'''

	assert type(coefs) == list
	assert type(b) == int and b > 0
	for c in coefs:
		assert type(c) == int and c > 0

	a_i = np.array(coefs)
	b = np.array(b)
	x_max = (b / a_i).astype(int) + 1
	a_x = []

	for i in range(a_i.shape[0]):
		a_x.append(np.arange(x_max[i]) * np.array([a_i[i]]))

	lhs_sum = 0
	for i in range(a_i.shape[0]):
		xi_shape = []
		for j in range(a_i.shape[0]):
			if j == i:
				xi_shape.append(x_max[i])
			else:
				xi_shape.append(1)
		lhs_sum = lhs_sum + a_x[i].reshape(tuple(xi_shape))

	solutions = []
	for i in np.array(np.where(lhs_sum == b)).T:
		solutions.append(tuple(i))

	return solutions
