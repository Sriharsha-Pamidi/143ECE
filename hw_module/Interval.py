class Interval(object):
	def __init__(self, a, b):
		"""
		:a: integer
		:b: integer
		"""
		assert a < b
		assert isinstance(a, int)
		assert isinstance(b, int)
		self._a = a
		self._b = b

	def __repr__(self):
		rep = 'Interval(' + str(self._a) + ',' + str(self._b) + ')'
		return rep

	def __eq__(self, other):
		if self._a == other._a and self._b == other._b:
			return True
		else:
			return False

	def __lt__(self, other):
		if self._a <= other._a < self._b <= other._b:
			return True
		else:
			return False

	def __gt__(self, other):
		if other._a < self._a < other._b < self._b:
			return True
		else:
			return False

	def __ge__(self, other):
		# other is inside self
		if self._a <= other._a and self._b >= other._b:
			return True
		else:
			return False

	def __le__(self, other):
		# self is inside other
		if self._a >= other._a and self._b <= other._b:
			return True

	def __add__(self, other):
		if self <= other:
			return other
		if self >= other:
			return self
		if self < other:
			return Interval(self._a, other._b)
		if self > other:
			return Interval(other._a, self._b)

		return [self, other]
