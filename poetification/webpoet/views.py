from django.shortcuts import render
from django.template  import RequestContext, loader
from django.shortcuts import render, render_to_response, redirect
from django.http import *
from models import *

def index(request):
    return redirect('home')

# Create your views here.
def home(request):
    template = loader.get_template('webpoet/index.html')
    poems = Poem.objects.all()
    context = RequestContext(request, {'poems' : poems})
    return HttpResponse(template.render(context))

# def new(request):
#     template = loader.get_template('webpoet/new.html')
#     context = RequestContext(request, {})
#     return HttpResponse(template.render(context))
