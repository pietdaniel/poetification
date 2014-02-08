class PoemLine:
	"""A line in the poem"""

	def __init__(self, syl, family, rhymes):
		self.syl = syl
		self.family = family
		self.rhymes = rhymes

	def __init__(self):
		self.syl = 0
		self.family = ""
		self.rhymes = {}

