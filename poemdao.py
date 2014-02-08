import json
from poemline import PoemLine
from itertools import combinations

"""
	General data access object for the poem
	Handles individual lines and poem families
"""

class Poem:
	def __init__(self,rhyme_families,lines, syls):
		self.rhyme_families = rhyme_families
		self.lines = lines
		self.syllables = syls

	def __init__(self):
		# number of rhyme families in poem
		self.rhyme_families = []
		# array of poemline objects
		self.lines = []
		# syllables and lines count
		self.syllables = {}

	"""
		sets the lines based on raw_json passed
		makes the rhyme families
		sets syllable counts
	"""
	def create_poem(self, raw_json):
		data = json.loads(raw_json)
		for i in data:
			pline = PoemLine()
			pline.create_poemline(data[i])
			self.lines.append(pline)
		listOfSets = []
		for poem in self.lines:
			listOfSets.append(poem.rhymes)
			try:
				self.syllables[poem.syl] += 1
			except Exception as e:
				self.syllables[poem.syl] = 1
		self.make_families(listOfSets)

	"""
		Takes two sets, returns percentage of similiar words
	"""
	def match_percentage(self, listA,listB):
		if (len(listA)+len(listB))==0:
			return 0
		else:
			return (2.*len(listA&listB))/(len(listA)+len(listB))

	"""
		Takes a list of sets 
		returns a map of family to set union
	"""
	def make_families(self, listOfSets):
		seen = {}
		set_num = 0
		families = {}
		for s in listOfSets:
			seen[set_num]=[s,False]
			set_num+=1
		combs = combinations(listOfSets, 2)
		q = 0
		for i in combs:
			if self.match_percentage(i[0],i[1]) > .49:
				families[q]=i[0]|i[1]
				q+=1
				self.mark_seen(i[0],seen)
				self.mark_seen(i[1],seen)
			elif (len(i[0])+len(i[1]))==0:
				self.mark_seen(i[0],seen)
				self.mark_seen(i[1],seen)
		for s in seen:
			if (not seen[s][1]):
				families[q]=seen[s][0]
				q+=1
		self.rhyme_families = families

	"""
		Helper function for make_families
	"""
	def mark_seen(self, setA,seen):
		for s in seen:
			if (seen[s][0]==setA):
				seen[s][1]=True

