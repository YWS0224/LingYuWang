from django.shortcuts import render

from TV_Play.models import *
# Create your views here.
def Tv_play(request):
    Tv = Tv_Play.objects.all()
    return Tv

