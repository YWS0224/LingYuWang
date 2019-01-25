from django.shortcuts import render
from .models import *

# Create your views here.


def select_ZhuanFang(request):
    ZList_XD = Find_ZhuanFang.objects.all()
    return ZList_XD
