from django.http import HttpResponseRedirect
from django.conf import settings
from twython import Twython
import re
import urllib2

from django.shortcuts import render
from django.template  import RequestContext, loader
from django.shortcuts import render, render_to_response, redirect
from django.http import *
from models import *
import json

from twython import Twython


def index(request):
    return redirect('home')

# Create your views here.
def home(request):
    template = loader.get_template('webpoet/index.html')
    poems = Poem.objects.all()
    context = RequestContext(request, {'poems' : poems})
    return HttpResponse(template.render(context))

def fbauth(request):
    redirect_state = request.GET['redirect_state']
    redirect_uri = "http://127.0.0.1/complete/facebook/?redirect_state="+redirect_state
    get_access_token = "https://graph.facebook.com/oauth/access_token?client_id="+settings.FACEBOOK_APP_ID+"&redirect_uri="+redirect_uri+"&client_secret="+settings.FACEBOOK_API_SECRET+"&code="+request.GET['code']
    contents = urllib2.urlopen(get_access_token)
    response = contents.read()
    contents.close()
    re_find = re.search("(?<=\=)(.*?)(?=\&)", response)
    access_token = re_find.group(0)
    get_posts_request = "https://graph.facebook.com/me/statuses?fields=message&access_token="+access_token
    contents = urllib2.urlopen(get_posts_request).read()
    result = json.loads(contents)
    poems = Poem.getHaiku(Poem.fromFacebookFeed(result['data']))
    return HttpResponse(poems)

def fbaccess(request):
    print 'fbaccess'

def twauth(request, redirect_url="/twaccess/"):
    twitter = Twython(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
    auth = twitter.get_authentication_tokens(callback_url='http://127.0.0.1/twaccess/')
    OAUTH_TOKEN = auth['oauth_token']
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    request.session['oauth_token'] = OAUTH_TOKEN
    request.session['oauth_token_secret'] = OAUTH_TOKEN_SECRET
    return HttpResponseRedirect(auth['auth_url'])

def twaccess(request, redirect_url="/home"):
    oauth_verifier = request.GET['oauth_verifier']
    twitter = Twython(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, request.session['oauth_token'], request.session['oauth_token_secret'])
    final_step = twitter.get_authorized_tokens(oauth_verifier)
    OAUTH_TOKEN = final_step['oauth_token']
    OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
    twitter = Twython(settings.TWITTER_CONSUMER_KEY,settings.TWITTER_CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

    poems = Poem.fromTwitterTimeline(twitter.get_user_timeline())
    return HttpResponse(poems)


    # STUB RETURN HTTPRESPONSE AND SHIT
