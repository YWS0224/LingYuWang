from django.shortcuts import render
from Welfare.models import *


# Create your views here.


# 查询所有福利信息
def Find_Welfare(request):
    w_info = Find_welfare_Info.objects.all()
    return w_info


# 根据id 查询福利信息
def Welfare_Byid(request, Wid):
    w_info = Find_welfare_Info.objects.filter(id = Wid)
    return w_info
