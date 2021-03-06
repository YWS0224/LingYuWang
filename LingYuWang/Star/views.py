from django.shortcuts import render
from Star.models import *
from django.db.models import Q
# Create your views here.

# 查询排序不为1的明星
def Find_Star(request):
    Find_list = Find_Star_Info.objects.filter(~Q(Star_Index=1))
    return Find_list

# 查询排序为1的明星
def Find_Star_first(request):
    Star_first = Find_Star_Info.objects.filter(Star_Index=1)
    return Star_first

# 根据Id查询明星
def Find_Star_ById(request, Sid):
    Star = Find_Star_Info.objects.filter(id=Sid)
    return Star

# 查询所有明星信息
def Find_All(request):
    Star_all = Find_Star_Info.objects.all()
    return Star_all
