import json
from poemline import PoemLine
from itertools import combinations

"""
    General data access object for the poem
    Handles individual lines and poem families
"""

class Poem:
    def __init__(self,rhyme_families,lines, syls):
        self.rhyme_families = rhyme_families
        self.lines = lines
        self.syllables = syls

    def __init__(self):
        # number of rhyme families in poem
        self.rhyme_families = []
        # array of poemline objects
        self.lines = []
        # syllables and lines count
        self.syllables = {}

    """
        sets the lines based on raw_json passed
        makes the rhyme families
        sets syllable counts
    """
    def create_poem(self, raw_json):
        data = json.loads(raw_json)
        for i in data:
            pline = PoemLine()
            pline.create_poemline(data[i])
            self.lines.append(pline)
        self.make_fam()
        for poem in self.lines:
            try:
                self.syllables[poem.syl].append(poem)
            except Exception as e:
                self.syllables[poem.syl] = [poem]
        

    """
        Takes two sets, returns percentage of similiar words
    """
    def match_percentage(self, listA, listB):
        if (len(listA)+len(listB))==0:
            return 0
        else:
            return (2.*len(listA&listB))/(len(listA)+len(listB))

    """
        WORKS BUT DEPRECATED
    """
    def make_families(self):
        seen = {}
        set_num = 0
        families = {}
        for s in self.lines:
            seen[set_num]=[s.rhymes,False]
            set_num+=1
        combs = combinations(self.lines, 2)
        q = 0
        for i in combs:
            if self.match_percentage(i[0].rhymes,i[1].rhymes) > .49:
                families[q]=i[0].rhymes|i[1].rhymes
                q+=1
                self.mark_seen(i[0].rhymes,seen)
                self.mark_seen(i[1].rhymes,seen)
            elif (len(i[0].rhymes)+len(i[1].rhymes))==0:
                self.mark_seen(i[0].rhymes,seen)
                self.mark_seen(i[1].rhymes,seen)
        for s in seen:
            if (not seen[s][1]):
                families[q]=seen[s][0]
                q+=1
        self.rhyme_families = families

    def make_fam(self):
        q=0
        for line in self.lines:
            for l2 in self.lines:
                if (line != l2):
                    print line.rhymes
                    print l2.rhymes
                    print self.match_percentage(line.rhymes,l2.rhymes)
                    if (self.match_percentage(line.rhymes,l2.rhymes) > .01):
                        line.family.append(q)
                        l2.family.append(q)
                        q+=1
                    elif ((len(line.rhymes)+len(l2.rhymes))==0):
                        line.family.append(-1)
                        l2.family.append(-1)


    """
        Helper function for make_families
    """
    def mark_seen(self, setA, seen):
        for s in seen:
            if (seen[s][0]==setA):
                seen[s][1]=True
                seen[s][1]
