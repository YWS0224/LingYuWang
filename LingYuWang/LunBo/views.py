from django.shortcuts import render
from django.db.models import Q
from LunBo.models import *


# Create your views


# 轮播图
def Lun_Bo(request):
    LunBo_T = LunBo.objects.filter(~Q(id=1))
    return LunBo_T


def Lun_Bo_First(request):
    Lun_First = LunBo.objects.filter(id=1)
    return Lun_First
