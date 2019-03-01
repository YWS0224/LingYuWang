from django.shortcuts import render
from django.db.models import Q
from .models import *

# Create your views here.


# 查询排序不为1的电影
def select_Movie(request):
    MList = Movie.objects.filter(~Q(Movie_Index=1))
    return MList


# 根据Id查询电影
def select_Movie_ById(request, Mid):
    MovieInfo = Movie.objects.filter(id=Mid)
    return MovieInfo


# 查询排序为1的电影
def select_Movie_first(request):
    Movie_first = Movie.objects.filter(Movie_Index=1)
    return Movie_first


# 查询所有电影
def select_all(request):
    Movie_all = Movie.objects.all()
    return Movie_all
