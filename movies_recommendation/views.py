#from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.http.request import QueryDict
from django.template import context, loader
from django.shortcuts import render

from .models import hybrid , Movies

def index(request):
    template = loader.get_template('movies_recommendation/index.html')
    context = {'title_movies': Movies.title}
    return HttpResponse(template.render(context, request=request))

def movies_recommendation(request):
    query = request.GET['liste']
    test = hybrid(1, query)
    context = {'test': test}
    return render(request, 'movies_recommendation/list.html', context)