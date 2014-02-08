import nltk
from itertools import combinations
from nltk.corpus import cmudict

"""
	finds rhymes for a given word 
"""
def rhyme(inp, level):
	entries = cmudict.entries()
	syllables = [(word, syl) for word, syl in entries if word == inp]
	rhymes = []
	for (word, syllable) in syllables:
		rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
	return set(rhymes)


"""
	Takes two sets, returns percentage of similiar words
"""
def match_percentage(listA,listB):
	if (len(listA)+len(listB))==0:
		return 0
	else:
		return (2.*len(listA&listB))/(len(listA)+len(listB))

"""
	Takes a list of sets 
	returns a map of family to set union
"""
def make_families(listOfSets):
	seen = {}
	set_num = 0
	for s in listOfSets:
		seen[set_num]=[s,False]
		set_num+=1

	mpr = {}
	combs = combinations(listOfSets, 2)
	q = 0
	for i in combs:
		if match_percentage(i[0],i[1]) > .49:
			mpr[q]=i[0]|i[1]
			q+=1
			mark_seen(i[0],seen)
			mark_seen(i[1],seen)
		elif (len(i[0])+len(i[1]))==0:
			mark_seen(i[0],seen)
			mark_seen(i[1],seen)
	for s in seen:
		if (not seen[s][1]):
			mpr[q]=seen[s][0]
			q+=1
	return mpr

"""
	Helper function for make_families
"""
def mark_seen(setA,seen):
	for s in seen:
		if (seen[s][0]==setA):
			seen[s][1]=True

