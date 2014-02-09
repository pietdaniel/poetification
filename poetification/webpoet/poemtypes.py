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
	def makeHaiku(self, families):
		for family in families.keys():
			print families[family][1][1]
			syl = families[family][1][1].syllables
			if syl == 5:
				if (self.first == ""):
					self.first = families[family][0]
				else:
					self.third = families[family][0]
			if syl == 7:
				self.second == ""
		if (self.first != "" and self.second != "" and self.third != ""):
			return [self.first,self.second,self.third]
		else:
			return False





class General:
	pass
