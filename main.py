from poemdao import Poem

raw_json=open("test.json").read()

poem = Poem()

print 'begin'
poem.create_poem(raw_json)
print 'end'

