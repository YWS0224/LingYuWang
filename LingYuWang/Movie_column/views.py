from django.shortcuts import render
from .models import *

# Create your views here.


def select_Movie(request):
    MList = Movie.objects.all()
    return MList


def select_Movie_Xiaode(request):
    MList_xiaode = Movie_xiaode.objects.all()
    return MList_xiaode
