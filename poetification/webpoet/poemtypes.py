from models import *
import models as m

class Poem(object):
    # Each poem is stored as a list of lines
    # in the list self.poems
    style = "N/A"
    poems = []

    @staticmethod
    def make(posts):
        poetry = []
        poetry += Haiku(posts).emit()
        poetry += Dodoitsu(posts).emit()
        poetry += Limerick(posts).emit()
        poetry += Sonnet(posts).emit()
        poetry += Other(posts).emit()
        if (len(poetry)):
            return poetry
        else:
            poetry.append(['Sorry',['No poems were found']])
            return poetry


    def emit(self):
        '''
        Returns a tuple of the poem type and the list of poems
        '''
        if self.style and self.poems <> []:
            return [(self.style, self.poems)]
        else:
            return []

class Other(Poem):
    style = "Other"
    def __init__(self, posts):
        poem = []
        fhash = posts.familyhash.copy()
        for family in fhash.keys():
            flist = fhash[family]
            while len(flist) >= 2:
                # take out two elements
                poem.append(flist.pop().text)
                poem.append(flist.pop().text)

        try:
            for i in range(0, len(poem), 4):
                poem[i+1], poem[i+2] = poem[i+2], poem[i+1]
        except: pass

        self.poems.append(poem)

        
class Pantoum(Poem):
    pass

class Sonnet(Poem):
    style = "Sonnet"
    def __init__(self, posts):
        poem = []
        fhash = posts.familyhash.copy()
        # Needs 6 pairs of cardinality 2
        for family in fhash.keys():
            flist = fhash[family]
            while len(flist) >= 2:
                poem.append(flist.pop().text)
                poem.append(flist.pop().text)

        if len(poem) < 14:
            # Invalid poem, do not append to list, return
            return

        poem[1], poem[2] = poem[2], poem[1]
        poem[5], poem[6] = poem[6], poem[5]
        poem[9], poem[10] = poem[10], poem[9]
        poem = poem[:13]
        self.poems += [poem]

class Limerick(Poem):
    style = "Limerick"
    def __init__(self, posts):
        m = []
        n = []
        fmap = posts.familyhash.copy()
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
            return #Not a poem!

        self.poems += [[m[0],m[1],n[0],n[1],m[1]]]

class Dodoitsu(Poem):
    style = 'Dodoitsu'
    def __init__(self, posts):
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
                self.poems += [[one,two,three,four]]

class Rondeau(Poem):
    pass

class Haiku(Poem):
    style = 'Haiku'
    def __init__(self, posts):
        first = ""
        second = ""
        third = ""

        frst=False
        scnd=False
        thrd=False
        for line in posts.lines:
            if (line == None):
                continue
            syl = line.syllables
            if syl == 5:
                if (first == ""):
                    frst = True
                    first = line.text
                else:
                    thrd = True
                    third = line.text
            if syl == 7 and not scnd:
                scnd = True
                second = line.text
            if (frst and scnd and thrd):
                self.poems += [[first,second,third]]
