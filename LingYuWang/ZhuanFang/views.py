from django.shortcuts import render
from .models import *
from django.db.models import Q


# Create your views here.


# 查询全部
def select_ZhuanFang(request):
    ZList_XD = Find_ZhuanFang.objects.all()
    return ZList_XD


# 根据ID查询专访
def Find_ZhuanFang_ByID(request, Zid):
    ZhuanFang_Find = Find_ZhuanFang.objects.filter(id=Zid)
    return ZhuanFang_Find


# 查询排序为1的专访
def ZhuanFang_first(request):
    ZhuanFang_first_info = Find_ZhuanFang.objects.filter(ZhuanFang_Index=1)
    return ZhuanFang_first_info


# 查询排序不为1的专访
def ZhuanFang_Not1(request):
    ZhuanFang_info = Find_ZhuanFang.objects.filter(~Q(ZhuanFang_Index=1))
    return ZhuanFang_info
