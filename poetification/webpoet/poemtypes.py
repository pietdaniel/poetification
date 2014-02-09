from models import *
import models as m
# class PoemType(object):
#     pattern = {}
#     def check_pattern(self, fams):

        
class Pantoum:
    def pred(posts):
        pass


class Sonnet:
    def pred(self, posts):
        m = []
        fhash = posts.familyhash.copy()
        # print fhash
        # Needs 6 pairs of cardinality 2
        for family in fhash.keys():
            flist = fhash[family]
            while len(flist) >= 2:
                # take out two elements
                m.append(flist.pop().text)
                m.append(flist.pop().text)

        if len(m) < 14:
            return False

        m[1], m[2] = m[2], m[1]
        m[5], m[6] = m[6], m[5]
        m[9], m[10] = m[10], m[9]
        m = m[:13]

        return m

class Limerick:
    def pred(self, posts):
    	m = []
    	n = []
        fmap = posts.familyhash.copy()
        # print fhash
        # Needs 1 pairs of syl 5-7
        # Needs 3-tuple of syl 8-10
        for family in fmap.keys():
            flist = fmap[family]
            if len(flist) >= 3:
            	while (len(m)<=2):
            		try:
	            		ele = flist.pop()
	            	except Exception as e:
	            		break
	            	if (ele.syllables > 7 and  ele.syllables < 11):
	            		m.append(ele.text)

	    for family in fmap.keys():
			flist = fmap[family]
            if (len(flist)) >= 2:
            	while(len(n)<=1):
            		try:
            			ele = flist.pop()
            		except Exception as e:
	            		break
            		if (ele.syllables > 4 and ele.syllables < 8):
            			n.append(ele.text)


        if (len(m)+len(n)) < 5:
            return False

        return [m[0],m[1],n[0],n[1],m[1]]

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
