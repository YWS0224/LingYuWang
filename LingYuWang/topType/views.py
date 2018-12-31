from django.shortcuts import render
from topType.models import *


# Create your views here.

# 顶部分类

def top_Type(request):
    TopType1 = Top_Type.objects.all()
    return TopType1
