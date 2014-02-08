"""
	General data access object for the poem
	Handles individual lines and poem families
"""

class Poem:

	def __init__(self,rhyme_families,lines):
		self.rhyme_families = rhyme_families
		self.lines = lines

	def __init__(self):
		# number of rhyme families in poem
		self.rhyme_families = []
		# array of poemline objects
		self.lines = []
