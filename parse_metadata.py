import json
import re
from rhyme import rhyme
from poemline import PoemLine
from syllable import line_syl

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
	my_line.rhymes = rhyme(string.split()[-1], -1)
	my_line.rhymeLevel = -1
	return my_line

print create_poemline("I saw a dog at the park")