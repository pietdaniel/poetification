from django.db import models
from django.contrib.auth.models import User
import urllib, json
from lineutils import *
from collections import defaultdict

class Poem(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True)

    # expects a list of phrases
    @staticmethod
    def getFamilies(phrases):
        families = defaultdict(set)
        for p in phrases:
            words = remove_symbols(remove_urls(p)).split()
            
            lastword = RhymeWord.findWord(words[-1])

            if not lastword:
                continue 
            
            families[lastword.rhyme_phoneme].append(one, two)

        return families


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
            
