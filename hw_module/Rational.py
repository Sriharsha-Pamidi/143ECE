import math


class Rational(object):
	def __init__(self, a, b):
		"""
		:a: integer
		:b: integer
		"""
		assert isinstance(a, int)
		assert isinstance(b, int)
		self._numerator = a
		self._denominator = b

	def __repr__(self):
		if self._denominator == 1:
			return str(self._numerator)
		if self._numerator % self._denominator == 0:
			return str(int(self._numerator / self._denominator))
		else:
			g = math.gcd(self._numerator, self._denominator)
			if self._denominator < 0:
				g = -g
			self._numerator //= g
			self._denominator //= g
			return '%s/%s' % (self._numerator, self._denominator)

	def __eq__(self, other):
		if isinstance(other, int):
			return self._numerator == other and self._denominator == 1
		if isinstance(other, float):
			return float(self) == other
		return self.__repr__() == other.__repr__()

	def __lt__(self, other):
		if isinstance(other, Rational):
			return self._numerator * other._denominator < self._denominator * other._numerator
		if isinstance(other, (int,float)):
			return float(self) < other
		else:
			return NotImplemented

	def __gt__(self, other):
		if isinstance(other, Rational):
			return self._numerator * other._denominator > self._denominator * other._numerator
		if isinstance(other, (int,float)):
			return float(self) > other
		else:
			return NotImplemented

	def __ge__(self, other):
		if isinstance(other, Rational):
			return self._numerator * other._denominator >= self._denominator * other._numerator
		if isinstance(other, (int,float)):
			return float(self) >= other
		else:
			return NotImplemented

	def __le__(self, other):
		if isinstance(other, Rational):
			return self._numerator * other._denominator <= self._denominator * other._numerator
		if isinstance(other, (int,float)):
			return float(self) <= other
		else:
			return NotImplemented

	def __add__(self, other):
		if isinstance(other, Rational):
			return Rational(self._numerator * other._denominator + other._numerator * self._denominator, self._denominator * other._denominator)
		elif isinstance(other, (int,float)):
			return Rational(other*self._denominator + self._numerator,self._denominator)
		return NotImplemented

	def __radd__(self, other):
		if isinstance(other, Rational):
			return Rational(self._numerator * other._denominator + other._numerator * self._denominator, self._denominator * other._denominator)
		elif isinstance(other, (int,float)):
			return Rational(other*self._denominator + self._numerator,self._denominator)
		return NotImplemented

	def __sub__(self, other):
		if isinstance(other, Rational):
			return Rational(self._numerator * other._denominator - other._numerator * self._denominator, self._denominator * other._denominator)
		elif isinstance(other, (int, float)):
			return Rational(self._numerator - other * self._denominator, self._denominator)
		return NotImplemented

	def __rsub__(self, other):
		if isinstance(other, Rational):
			return Rational(other._numerator * self._denominator - self._numerator * other._denominator, self._denominator * other._denominator)
		elif isinstance(other, (int, float)):
			return Rational(other * self._denominator - self._numerator, self._denominator)
		return NotImplemented

	def __mul__(self, other):
		if isinstance(other, Rational):
			return Rational(self._numerator * other._numerator, self._denominator * other._denominator)
		elif isinstance(other, (int,float)):
			return Rational(other*self._numerator,self._denominator)
		return NotImplemented

	def __rmul__(self, other):
		if isinstance(other, Rational):
			return Rational(self._numerator * other._numerator, self._denominator * other._denominator)
		elif isinstance(other, (int,float)):
			return Rational(other*self._numerator,self._denominator)
		return NotImplemented

	def __truediv__(self, other):
		if isinstance(other, Rational):
			return Rational(self._numerator * other._denominator, self._denominator * other._numerator)
		elif isinstance(other, (int,float)):
			return Rational(self._numerator, other*self._denominator)
		return NotImplemented

	def __rtruediv__(self, other):
		if isinstance(other, Rational):
			return Rational(self._denominator * other._numerator, self._numerator * other._denominator)
		elif isinstance(other, (int,float)):
			return Rational(other*self._denominator, self._numerator)
		return NotImplemented

	def __neg__(self):
		return Rational(-self._numerator, self._denominator)

	def __float__(self):
		return float(self._numerator / self._denominator)

	def __int__(self):
		return self._numerator // self._denominator
