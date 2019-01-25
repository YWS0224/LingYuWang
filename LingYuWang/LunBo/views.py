from django.shortcuts import render
from django.db.models import Q
from LunBo.models import *


# Create your views


# 轮播图
def Lun_Bo(request):
    LunBo_T = LunBo.objects.filter(~Q(LunBo_Index=1))
    return LunBo_T


def Lun_Bo_First(request):
    Lun_First = LunBo.objects.filter(LunBo_Index=1)
    return Lun_First


def LunBo_ById(request, Lid):
    LunBo_Info = LunBo.objects.filter(id=Lid)
    return LunBo_Info
