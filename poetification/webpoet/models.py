from django.db import models
from django.contrib.auth.models import User
import urllib, json
from lineutils import *
from collections import defaultdict
import poemtypes

class Poem(models.Model):
    # expects a list of phrases
    @staticmethod
    def getFamilies(phrases):
        families = defaultdict(list)
        for p in phrases:
            words = remove_symbols(remove_urls(p)).split()
            if len(words) == 0:
                continue

            lastword = RhymeWord.findWord(words[-1])

            if not lastword:
                continue 
            
            families[lastword.rhyme_phoneme].append( p )

        return families

    @staticmethod
    def fromTwitterTimeline(timeline):
        families = Poem.getFamilies([tweet['text'] for tweet in timeline])
        # print families
        for family in families.keys():
            print len(families[family]), family, families[family]
        return families

    @staticmethod
    def fromFacebookFeed(feed):
        families = Poem.getFamilies([line['message'] for line in feed])
        # print families
        for family in families.keys():
            print len(families[family]), family, families[family]
        return families

    @staticmethod
    def getHaiku(families):
        haiku = poemtypes.Haiku()
        return haiku.makeHaiku(families)




class Line(models.Model):
    poem = models.ForeignKey(Poem)
    text = models.CharField(max_length=2048, blank=True, null=False)
    syllables = models.IntegerField()


class RhymeWord(models.Model):
    RBRAIN="http://rhymebrain.com/talk?function=getWordInfo&word="

    word = models.CharField(max_length=128)
    syllables = models.IntegerField(db_index=True, null=False)
    rhyme_phoneme = models.CharField(max_length=32, 
                                     blank=False, 
                                     db_index=True,
                                     null=False)
    class Meta:
        unique_together = ['word', 'syllables', 'rhyme_phoneme']


    def rhymesWith(self, other):
        return other.rhyme_phoneme == self.rhyme_phoneme
    

    @staticmethod
    def findWord(word):
        try:
            rw = RhymeWord.objects.get(word=word)
        except:
            f = urllib.urlopen(RhymeWord.RBRAIN + word)
            phonemes = json.loads(f.read())['pron'].split()
            rc = re.compile(r'\d{1}')
            vowels = filter(lambda x: rc.search(x[1]), enumerate(phonemes))
            syllables = len(vowels)
            if syllables == 0:
                rw = None
            else:
                lastphonemes = phonemes[vowels[-1][0]:]
                rhyme_phoneme = rc.sub('', ''.join(lastphonemes))
                rw = RhymeWord(word=word,
                               syllables=syllables,
                               rhyme_phoneme=rhyme_phoneme)
                rw.save()
        finally:
            return rw
            
