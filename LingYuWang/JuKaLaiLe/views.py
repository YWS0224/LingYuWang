from django.shortcuts import render
from JuKaLaiLe.models import *
# Create your views here.

def Jukalaile_find_all(request):
    Juka = Jukalai_L.objects.all()
    return Juka

def Jukalaile_find_all_Xd(request):
    Juka_Xd = Jukalai_L_Xd.objects.all()
    return Juka_Xd