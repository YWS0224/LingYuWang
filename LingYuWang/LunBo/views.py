from django.shortcuts import render
from LunBo.models import *


# Create your views
def Lun_Bo(request):
    LunBo_T = LunBo.objects.all()
    return LunBo_T
