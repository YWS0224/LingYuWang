from django.shortcuts import render
from Star.models import *
# Create your views here.


def Find_Star(request):
    Find = Find_Star_Info.objects.all()
    return Find


def Find_Star_xd(request):
    Find_xd = Find_Star_Info_xd.objects.all()
    return Find_xd