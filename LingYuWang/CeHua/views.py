from django.shortcuts import render
from CeHua.models import *
# Create your views here.


# 查询全部
def select_CeHua(request):
    Cehua = CeHua_photos.objects.all()
    return Cehua


# 根据ID查询
def Find_CeHua_ByID(request, Cid):
    Find_CH = CeHua_photos.objects.filter(id=Cid)
    return Find_CH