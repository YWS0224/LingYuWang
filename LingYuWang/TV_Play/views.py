from django.shortcuts import render
from django.db.models import Q
from TV_Play.models import *
# Create your views here.


def Tv_play(request):
    Tv_list = Tv_Play.objects.filter(~Q(TV_Index=1))
    return Tv_list


def Tv_first(request):
    Tv_first = Tv_Play.objects.filter(TV_Index=1)
    return Tv_first


def Tv_ById(request, Tid):
    Tv = Tv_Play.objects.filter(id=Tid)
    return Tv
