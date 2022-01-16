from hw_module.Rational import Rational


def square_root_rational(rational_x, abs_tol=Rational(1, 1000)):
	'''Using your Rational class for representing rational numbers, write a function square_root_rational
	which takes an input rational number x and returns the square root of x to absolute precision abs_tol.
	Your function should return a Rational number instance as output'''

	assert type(rational_x) == Rational
	assert type(abs_tol) == Rational

	x = float(rational_x)
	low = 0
	high = max(1.0, x)
	y = (high + low) / 2.0
	while abs(y ** 2 - x) >= float(abs_tol):
		if y ** 2 < x:
			low = y
		else:
			high = y
		y = (high + low) / 2.0
	return Rational(*y.as_integer_ratio())
