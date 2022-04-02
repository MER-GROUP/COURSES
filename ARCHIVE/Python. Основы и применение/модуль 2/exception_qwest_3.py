class NonPositiveError(Exception):
	pass

class PositiveList(list):
	def append(self, x):
		if 0 < x:
			super().append(x)
		else:
			raise NonPositiveError