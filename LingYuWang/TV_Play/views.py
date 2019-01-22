from django.shortcuts import render

from TV_Play.models import *
# Create your views here.
def Tv_play(request):
    Tv = Tv_Play.objects.all()
    return Tv


def Tv_play_xd(request):
    Tv_xd = Tv_Play_xd.objects.all()
    return Tv_xd

