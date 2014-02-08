from utils import remove_urls
from utils import remove_symbols
from rhyme import rhyme
from syllable import line_syl

class PoemLine:
	"""A line in the poem"""

	RHYME_LEVEL = 1

	def __init__(self, syl, family, rhymes, originalString, cleanString):
		self.syl = syl
		self.family = family
		self.rhymes = rhymes
		self.originalString = originalString
		self.cleanString = cleanString

	def __init__(self):
		self.originalString = ""
		self.cleanString = ""
		self.syl = 0
		self.family = []
		self.rhymes = {}

	def create_poemline(self, string):
		# original text
		self.originalString = string
		# texts without symbols or urls
		self.cleanString = remove_symbols(remove_urls(string))
		# number of syllables in line
		self.syl = line_syl(self.cleanString)
		# rhymes against last word
		self.rhymes = rhyme(string.split()[-1], self.RHYME_LEVEL)