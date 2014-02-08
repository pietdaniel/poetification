import json
import re
from time import time
from rhyme import make_families
from rhyme import rhyme
from poemline import PoemLine
from poemdao import Poem
from syllable import line_syl

RHYME_LEVEL = 4

raw_data = open("test.json").read()
data = json.loads(raw_data)

lines = {}

def remove_urls(string):
	return re.sub(r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', ' ', string)

def remove_symbols(string):
	return re.sub(r'[^\w]', ' ', string)

def create_poemline(string):
	# create object
	my_line = PoemLine()
	# original text
	my_line.originalString = string
	# texts without symbols or urls
	my_line.cleanString = remove_symbols(remove_urls(string))
	# number of syllables in line
	my_line.syl = line_syl(my_line.cleanString)
	# rhymes against last word
	my_line.rhymes = rhyme(string.split()[-1], RHYME_LEVEL)
	my_line.rhymeLevel = RHYME_LEVEL
	return my_line

"""
	Takes raw_data
"""
def create_poem(raw_data):
	my_poem = Poem()
	data = json.loads(raw_data)
	for i in data:
		my_poem.lines.append(create_poemline(data[i]))
	listOfSets = []
	for poem in my_poem.lines:
		listOfSets.append(poem.rhymes)
	my_poem.rhyme_families = make_families(listOfSets)
	return my_poem

start = time()
test = create_poem(raw_data)
end = time()
print end - start

print test.rhyme_families
print len(test.rhyme_families)

