from django.shortcuts import render
from django.db.models import Q
from .models import *

# Create your views here.


def select_Movie(request):
    MList = Movie.objects.filter(~Q(Movie_Index=1))
    return MList


def select_Movie_ById(request, Mid):
    MovieInfo = Movie.objects.filter(id=Mid)
    return MovieInfo


def select_Movie_first(request):
    Movie_first = Movie.objects.filter(Movie_Index=1)
    return Movie_first
