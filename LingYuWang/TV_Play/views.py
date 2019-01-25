from django.shortcuts import render
from django.db.models import Q
from TV_Play.models import *
# Create your views here.


# 查询排序不为1的电视剧
def Tv_play(request):
    Tv_list = Tv_Play.objects.filter(~Q(TV_Index=1))
    return Tv_list


# 查询排序为1的电视剧
def Tv_first(request):
    Tv_first = Tv_Play.objects.filter(TV_Index=1)
    return Tv_first


# 根据id查询电视剧
def Tv_ById(request, Tid):
    Tv = Tv_Play.objects.filter(id=Tid)
    return Tv


# 查询所有电视剧信息
def Tv_all(request):
    Tv_all = Tv_Play.objects.all()
    return Tv_all
