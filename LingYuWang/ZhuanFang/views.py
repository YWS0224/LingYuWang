from django.shortcuts import render
from .models import *

# Create your views here.


def select_ZhuanFang(request):
    ZList = Find_ZhuanFang.objects.all()
    return ZList


def select_ZhuanFang_XD(request):
    ZList_XD = Find_ZhuanFang_XD.objects.all()
    return ZList_XD
