# import json
import re
# from time import time
# from rhyme import make_families
# from rhyme import rhyme
# from poemline import PoemLine
# from poemdao import Poem
# from syllable import line_syl

def remove_urls(string):
	return re.sub(r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', ' ', string)

def remove_symbols(string):
	return re.sub(r'[^\w]', ' ', string)




#DEPRECATED MOVED TO POEMDAO
# """
# 	Takes raw_data, adds the poem lines, creates the families
# """
# def create_poem(raw_data):
# 	my_poem = Poem()
# 	data = json.loads(raw_data)
# 	for i in data:
# 		my_poem.lines.append(create_poemline(data[i]))
# 	listOfSets = []
# 	for poem in my_poem.lines:
# 		listOfSets.append(poem.rhymes)
# 		try:
# 			my_poem.syllables[poem.syl] += 1
# 		except Exception as e:
# 			my_poem.syllables[poem.syl] = 1
# 	my_poem.rhyme_families = make_families(listOfSets)
# 	return my_poem


# start = time()
# test = create_poem(raw_data)
# end = time()
# print end - start

# print test.rhyme_families
# print len(test.rhyme_families)
# print test.syllables