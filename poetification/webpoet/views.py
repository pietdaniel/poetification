from django.contrib.auth import authenticate, login, logout as django_logout

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.urlresolvers import reverse
from twython import Twython

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

def auth(request, redirect_url="/access/"):
	twitter = Twython(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
	auth = twitter.get_authentication_tokens(callback_url='http://127.0.0.1/access/')
	OAUTH_TOKEN = auth['oauth_token']
	OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
	request.session['oauth_token'] = OAUTH_TOKEN
	request.session['oauth_token_secret'] = OAUTH_TOKEN_SECRET
	return HttpResponseRedirect(auth['auth_url'])

def access(request, redirect_url="/home"):
	oauth_verifier = request.GET['oauth_verifier']
	twitter = Twython(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, request.session['oauth_token'], request.session['oauth_token_secret'])
	final_step = twitter.get_authorized_tokens(oauth_verifier)
	OAUTH_TOKEN = final_step['oauth_token']
	OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
	twitter = Twython(settings.TWITTER_CONSUMER_KEY,settings.TWITTER_CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
	print twitter.get_user_timeline()
	# STUB RETURN HTTPRESPONSE AND SHIT

