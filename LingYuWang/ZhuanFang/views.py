from django.shortcuts import render
from .models import *


# Create your views here.


# 查询全部
def select_ZhuanFang(request):
    ZList_XD = Find_ZhuanFang.objects.all()
    return ZList_XD


# 根据ID查询专访
def Find_ZhuanFang_ByID(request, Zid):
    ZhuanFang_Find = Find_ZhuanFang.objects.filter(id=Zid)
    return ZhuanFang_Find