from django.shortcuts import render
from Yingpinshe.models import *


# Create your views here.

# 查询所有影评社信息
def Yingping_find_all(request):
    Yingping = Yingping_Star_Info.objects.all()
    return Yingping


# 根据Id查询影评信息
def YingPing_Byid(request, Yid):
    YingPing_Info = Yingping_Star_Info.objects.filter(id = Yid)
    return YingPing_Info


# 查询排序为1的影评信息
def YingPing_first(request):
    YingPing_first = Yingping_Star_Info.objects.filter(YingPing_Index=1)
    return YingPing_first
