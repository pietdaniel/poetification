import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
d = cmudict.dict()

def nsyl(word):
	return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]][0]

def testNsyl():
	print nsyl('test')==1
	print nsyl('double')==2
	print nsyl('america')==4