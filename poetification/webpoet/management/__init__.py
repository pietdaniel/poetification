# from django.db.models.signals import post_syncdb
# from nltk.corpus import cmudict
# import webpoet.models as M
# import nltk
# import re

# def cmudict_callback(sender, **kwargs):
#     # Match syllable inflection
#     rc = re.compile(r'\d{1}')
#     try:
#         entries = cmudict.entries()

#     except LookupError as le:
#         # download cmudict package!
#         nltk.download('cmudict')
#         entries = cmudict.entries()
        
#     finally:
#         for entry in entries:
#             phonemes = entry[1]
#             vowels = filter(lambda x: rc.search(x[1]), enumerate(phonemes))
#             syllables = len(vowels)
#             try:
#                 lastphonemes = phonemes[vowels[-1][0]:]
#             except: continue

#             rhyme_phoneme = rc.sub('', ''.join(lastphonemes))
#             try:
#                 rhymeword =\
#                     M.RhymeWord.objects.get(word=entry[0],
#                                             syllables=syllables,
#                                             rhyme_phoneme=rhyme_phoneme)
#             except:
#                 M.RhymeWord(word=entry[0],
#                             syllables=syllables,
#                             rhyme_phoneme=rhyme_phoneme).save()
                    
# post_syncdb.connect(cmudict_callback, sender=M)
