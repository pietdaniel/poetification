import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
d = cmudict.dict()
import json
import urllib

"""
Only works on actual words
"""
def nsyl(word):
	try:
		print d[word.lower()]
		out = [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]][0]
	except Exception as e:
		f = urllib.urlopen("http://rhymebrain.com/talk?function=getWordInfo&word="+word)
		a = json.loads(f.read())['pron'].split()
		d = []
		for word in a:
			d.append(word.encode("utf-8"))
		out = [len(list(y for y in x if isdigit(y[-1]))) for x in [d]][0]
	return out

def line_syl(line):
	words = line.split()
	count = 0
	for word in words:
		count += nsyl(word)
	return count

def testNsyl():
	print nsyl('test')==1
	print nsyl('double')==2
	print nsyl('america')==4

def testline_syl():
	line = "this has six sylables"
	print line_syl(line)==6