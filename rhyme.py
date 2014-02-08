import nltk
from nltk.corpus import cmudict

def rhyme(inp, level):
	entries = cmudict.entries()
	syllables = [(word, syl) for word, syl in entries if word == inp]
	rhymes = []
	for (word, syllable) in syllables:
		rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
	return set(rhymes)