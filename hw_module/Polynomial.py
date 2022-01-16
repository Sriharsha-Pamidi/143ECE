from collections import defaultdict


class Polynomial(object):
	def __init__(self, poly_dict):
		'''
		dict - keys are powers, values are coefficients
		'''
		assert type(poly_dict) == dict
		for i in poly_dict:
			assert type(i) == int
			assert type(poly_dict[i]) == int

		_dict = defaultdict(int)
		for key in sorted(poly_dict):
			_dict[key] = int(poly_dict[key])
		self._dict = _dict

	def __repr__(self):
		terms = []
		if all(value == 0 for value in self._dict.values()):
			return '0'
		for key in self._dict:
			if self._dict[key] != 0:
				if key == 0:
					terms.append(str(self._dict[key]))
				elif key == 1:
					if self._dict[key] == 1:
						terms.append("x")
					elif self._dict[key] == -1:
						terms.append("-x")
					else:
						terms.append(str(self._dict[key]) + "x")
				else:
					if self._dict[key] == 1:
						terms.append("x^(" + str(key) + ")")
					elif self._dict[key] == -1:
						terms.append("-x^(" + str(key) + ")")
					else:
						terms.append(str(self._dict[key]) + "x^(" + str(key) + ")")
		return ' + '.join(terms)

	def __eq__(self, other):
		if isinstance(other, int):
			if len(self._dict) == 0:
				return other == 0
			elif 0 in self._dict:
				for key in self._dict:
					if key != 0 and self._dict[key] != 0:
						return False
				return self._dict[0] == other
			else:
				return False
		return self.__repr__() == other.__repr__()

	def __add__(self, other):
		if isinstance(other, Polynomial):
			add_dict = defaultdict(int)
			for i in self._dict:
				add_dict[i] = self._dict[i]
			for i in other._dict:
				add_dict[i] += other._dict[i]
			return Polynomial(dict(add_dict))
		elif isinstance(other, int):
			add_dict = self._dict
			add_dict[0] += other
			return Polynomial(dict(add_dict))
		raise NotImplementedError

	def __radd__(self, other):
		return self + other

	def __sub__(self, other):
		return self + (-other)

	def __rsub__(self, other):
		return (-self) + other

	def __mul__(self, other):
		if isinstance(other, int):
			mul_dict = defaultdict(lambda: 1)
			for i in self._dict:
				mul_dict[i] = self._dict[i] * other
			return Polynomial(dict(mul_dict))
		if isinstance(other, Polynomial):
			mul_dict = defaultdict(int)
			for i in other._dict:
				for j in self._dict:
					mul_dict[i + j] += other._dict[i] * self._dict[j]
			return Polynomial(dict(mul_dict))
		raise NotImplementedError

	def __rmul__(self, other):
		return self * other

	def __truediv__(self, other):
		if isinstance(other, Polynomial):
			p = defaultdict(int)
			a = Polynomial(dict(self._dict))
			b = Polynomial(dict(other._dict))
			while any(value != 0 for value in a._dict.values()):
				if sum([1 for i in a._dict if a._dict[i] != 0]) < sum([1 for i in b._dict if b._dict[i] != 0]):
					raise NotImplementedError
				if a._dict[self.max_power(a._dict)] % b._dict[self.max_power(b._dict)] != 0:
					raise NotImplementedError
				p[self.max_power(a._dict) - self.max_power(b._dict)] = int(a._dict[self.max_power(a._dict)] / b._dict[
					self.max_power(b._dict)])
				temp = b * Polynomial(dict(p))
				a = self - temp
			return Polynomial(dict(p))
		if isinstance(other, int):
			p = defaultdict(int)
			for i in self._dict:
				if self._dict[i] % other != 0:
					raise NotImplementedError
				p[i] = int(self._dict[i] / other)
			return Polynomial(dict(p))
		raise NotImplementedError

	@staticmethod
	def max_power(_dict):
		return max(k for k, v in _dict.items() if v != 0)

	def __rtruediv__(self, other):
		return 1 / (self / other)

	def __neg__(self):
		return -1 * self

	def subs(self, other):
		res = 0
		for key in self._dict:
			res += self._dict[key] * pow(other, key)
		return res
