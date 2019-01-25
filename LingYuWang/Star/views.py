from django.shortcuts import render
from Star.models import *
from django.db.models import Q
# Create your views here.


def Find_Star(request):
    Find_list = Find_Star_Info.objects.filter(~Q(Star_Index=1))
    return Find_list


def Find_Star_first(request):
    Star_first = Find_Star_Info.objects.filter(Star_Index=1)
    return Star_first


def Find_Star_ById(request, Sid):
    Star = Find_Star_Info.objects.filter(id=Sid)
    return Star
