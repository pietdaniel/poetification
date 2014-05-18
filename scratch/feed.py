import  os
from twython import *

class TwitterFeed(object):
    def __init__(self):
        APP_KEY      = os.environ['P_APP_KEY']
        APP_SECRET   = os.environ['P_APP_SECRET']
        OAUTH_TOKEN  = os.environ['P_OAUTH_TOKEN']
        OAUTH_SECRET = os.environ['P_OAUTH_SECRET']

        self.t = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_SECRET)


    def tweets(self,user, tlimit=None):
        return [tt['text'] for tt in self.t.get_user_timeline(screen_name=user)]
