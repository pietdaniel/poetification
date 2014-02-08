class PoemLine:
	"""A line in the poem"""

	def __init__(self, syl, family, rhymes, originalString, cleanString, rhymeLevel):
		self.syl = syl
		self.family = family
		self.rhymes = rhymes
		self.originalString = originalString
		self.cleanString = cleanString
		self.rhymeLevel = rhymeLevel

	def __init__(self):
		self.originalString = ""
		self.cleanString = ""
		self.syl = 0
		self.family = ""
		self.rhymes = {}
		self.rhymeLevel = 0

