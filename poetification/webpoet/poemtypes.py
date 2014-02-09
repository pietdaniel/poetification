class Pantoum:
    pass

class Sonnet:
    pass

class Limerick:
    pass

class Dodoitsu:
    pass

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
