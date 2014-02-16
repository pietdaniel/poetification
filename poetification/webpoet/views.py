from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.template  import RequestContext, loader
from django.shortcuts import render, render_to_response, redirect
from django.http import *
from django.conf import settings
from urlparse import *
from twython import Twython
from models import *
from twython import Twython
from poemtypes import *

import re
import json
import urllib2

def index(request):
    return redirect('home')

# Create your views here.
def home(request):
    template = loader.get_template('webpoet/index.html')
    poems = PostList.objects.all()
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
    get_posts_request = "https://graph.facebook.com/me/statuses?fields=message&limit=50&access_token="+access_token
    contents = urllib2.urlopen(get_posts_request).read()
    result = json.loads(contents)
    poems = Poem.make(PostList.fromFacebookFeed(result))
    print poems
    template = loader.get_template('webpoet/poem.html')
    context = RequestContext(request, {'poems' : poems})
    return HttpResponse(template.render(context))

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
    result = twitter.get_user_timeline()
    # poems = PostList.fromTwitterTimeline(twitter.get_user_timeline())
    poems = Poem.make(PostList.fromTwitterTimeline(result))
    template = loader.get_template('webpoet/poem.html')
    context = RequestContext(request, {'poems' : poems})
    return HttpResponse(template.render(context))


def ghauth(request, redirect_url="/ghaccess/"):
    redirect_uri = request.build_absolute_uri(reverse('ghauth'))
    print "Redirecting to", redirect_uri
    auth_post_data = [('client_id',     settings.GITHUB_APP_ID),
                      ('client_secret', settings.GITHUB_API_SECRET),
                      ('code',          request.GET['code']),
                      ('redirect_uri',  redirect_uri)]
    result = urllib2.urlopen('https://github.com/login/oauth/access_token',
                             urllib.urlencode(auth_post_data))
    return HttpResponseRedirect(redirect_url + "?" + result.read())

def ghaccess(request):
    token = request.GET['access_token']
    repo_request = urllib2.Request('https://api.github.com/user/repos',
                                   headers = {'Authorization' : 'token ' + token})
    repos = json.loads(urllib2.urlopen(repo_request).read())

    all_messages = []

    for repo in repos:
        commits_url = 'https://api.github.com/repos/%s/commits' % repo['full_name']
        print commits_url
        try:
            commits_request =\
                urllib2.Request(commits_url,
                                headers = {'Authorization' : 'token ' + token})
            commits = json.loads(urllib2.urlopen(commits_request).read())
            all_messages += [c['commit']['message'] for c in commits]
        except:
            # Probably no commits for this repo, continue
            print "Failed to get commits for " + repo['full_name']

    print all_messages

    poems = Poem.make(PostList(all_messages))

    template = loader.get_template('webpoet/poem.html')
    context = RequestContext(request, {'poems' : poems})
    return HttpResponse(template.render(context))
        
