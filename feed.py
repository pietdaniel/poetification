import  os
from twython import *

# 'Pw0j9T6hW0OGFTwppSmlQ',
# 'BmwCFHwC6OTuWc2aPpFtLFxGb6XKCZtd9olQsPa3E',
# '817931958-CkNG0onLXBDeNwngnbtXOVyvA25sQv2uFL7SdoAw',
# 'qttMJ4uqhSRI25CBtnm9VTqlqTZicwTSVgpd0KezdTXgc'

class TwitterFeed(object):
    def __init__(self):
        APP_KEY      = os.environ['P_APP_KEY']
        APP_SECRET   = os.environ['P_APP_SECRET']
        OAUTH_TOKEN  = os.environ['P_OAUTH_TOKEN']
        OAUTH_SECRET = os.environ['P_OAUTH_SECRET']

        self.t = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_SECRET)


    def tweets(self,user, tlimit=None):
        return [tt['text'] for tt in self.t.get_user_timeline(screen_name=user,
                                                              limit=tlimit)]
