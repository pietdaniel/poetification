from poemdao import Poem

raw_json=open("test.json").read()

poem = Poem()

print 'begin'
poem.create_poem(raw_json)

for i in poem.syllables:
	for z in poem.syllables[i]:
		print z.originalString
		print z.family

print 'end'
