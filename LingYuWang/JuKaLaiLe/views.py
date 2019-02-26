from django.shortcuts import render
from JuKaLaiLe.models import *
from django.db.models import Q

# Create your views here.


# 查询剧咖来了排序不为1的信息
def Jukalaile_find_all(request):
    Juka = Jukalai_L.objects.filter(~Q(Jukalail_Index=1))
    return Juka


# 根据ID查询剧咖来了信息
def JuKaLaiLe_ById(request, Jid):
    JuKa_info = Jukalai_L.objects.filter(id=Jid)
    return JuKa_info


# 查询排序为1的剧咖来了信息
def JuKaiLaiLe_first(request):
    juka_first = Jukalai_L.objects.filter(Jukalail_Index=1)
    return juka_first
