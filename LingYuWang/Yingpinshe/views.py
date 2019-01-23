from django.shortcuts import render
from Yingpinshe.models import *


# Create your views here.

def Yingping_find_all(request):
    Yingping = Yingping_Star_Info.objects.all()
    return Yingping


def Yingping_find_all_Xd(request):
    Yingping_Xd = Yingping_Star_Info_xd.objects.all()
    return Yingping_Xd
