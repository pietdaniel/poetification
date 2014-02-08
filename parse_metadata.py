import json
import poemline

raw_data = open("test.json").read()
data = json.loads(raw_data)

lines = {}

for i in data:
	line = PoemLine()
	words = text.split()

	print data[i]