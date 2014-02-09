from django.db import models
from django.contrib.auth.models import User
import urllib, json
from lineutils import *
from collections import defaultdict
# from syllable import *
from poemtypes import Haiku
class PostList(models.Model):
    def __init__(self, phrases):
        self.lines = [Line.get_line(p) for p in phrases]

    @staticmethod
    def fromFacebookFeed(feed):
        postlist = PostList([msg['message'] for msg in feed])
        return postlist

    @staticmethod
    def fromTwitterTimeline(timeline):
        postlist = PostList([tweet['text'] for tweet in timeline])
        return postlist

    @staticmethod
    def getHaiku(posts):
        h = Haiku()
        return h.makeHaiku(posts)

class Line(models.Model):
    def __init__(self, phrase):
        self.text = phrase
        # if (len(self.clean_text) == 0):
        #     self.rw = ""
        # else:
        #     self.rw = RhymeWord.findWord(self.clean_text.split()[-1])

    @staticmethod
    def get_line(phrase):
        l = Line(phrase)
        if (len(l.clean_text) > 1):
            l.rw = RhymeWord.findWord(l.clean_text.split()[-1])
            return l
        else:
            return None

            
    def nsyl(self, word):
        word = RhymeWord.findWord(word)
        if not word:
            return 0
        else:
            return word.syllables
    
    @property
    def syllables(self):
        words = self.text.split()
        count = 0
        for word in words:
            count += self.nsyl(word)
        return count

    @property
    def clean_text(self):
        return remove_symbols(remove_urls(self.text))


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
            