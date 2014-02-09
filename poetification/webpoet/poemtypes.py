from models import *
import models as m
# class PoemType(object):
#     pattern = {}
#     def check_pattern(self, fams):

        

class Pantoum:
    pass

class Sonnet:
    pattern = {"A" : 0,
               "B" : 0,
               "A" : 0,
               "B" : 0,
               "C" : 0,
               "D" : 0,
               "C" : 0,
               "D" : 0,
               "E" : 0,
               "F" : 0,
               "E" : 0,
               "F" : 0,
               "G" : 0,
               "G" : 0}

    def pred(families):
        matches = {}

        for family in f.keys():
            while len(f[family]) >= 2:
                need -= 1
                matches['A1'] = f[family][0]
                matches['A2'] = f[family][1]


class Limerick:
    pass

class Dodoitsu:
    pattern = {"" : 7,
               "" : 7,
               "" : 7,
               "" : 5}

class Rondeau:
    pass

class Haiku:
	first = ""
	second = ""
	third = ""
	def makeHaiku(self, posts):
		frst=False
		scnd=False
		thrd=False
		for line in posts.lines:
			if (line == None):
				continue
			syl = line.syllables
			print syl
			print line.clean_text
			if syl == 5:
				if (self.first == ""):
					frst = True
					self.first = line.clean_text
				else:
					thrd = True
					self.third = line.clean_text
			if syl == 7 and not scnd:
				scnd = True
				self.second = line.clean_text
		if (frst and scnd and thrd):
			return [self.first,self.second,self.third]
		else:
			return False

class General:
	pass
