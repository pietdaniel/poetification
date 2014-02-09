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
	def makeDodoitsu(self, posts):
		one=""
		two=""
		three=""
		four=""
		one_seen=False
		two_seen=False
		three_seen=False
		four_seen=False
		for line in posts.lines:
			if (line==None):
				continue
			syl = line.syllables
			print line.clean_text + " : " + str(syl)
			if syl==5 and not four_seen:
				four=line.text
				four_seen=True
			elif syl==7:
				if not one_seen:
					one=line.text
					one_seen=True
					continue
				if not two_seen:
					two=line.text
					two_seen=True
					continue
				if not three_seen:
					three=line.text
					three_seen=True	
					continue
			if one_seen and two_seen and three_seen and four_seen:
				return [one,two,three,four]
		return False


 #    pattern = {"" : 7,
 #               "" : 7,
 #               "" : 7,
 #               "" : 5}

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
			print line.clean_text + " : " + str(syl)
			if syl == 5:
				if (self.first == ""):
					frst = True
					self.first = line.text
				else:
					thrd = True
					self.third = line.text
			if syl == 7 and not scnd:
				scnd = True
				self.second = line.text
			if (frst and scnd and thrd):
				return [self.first,self.second,self.third]
		return False

class General:
	pass
