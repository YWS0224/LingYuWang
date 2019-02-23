from django.shortcuts import render
from Star_Photos.models import *
# Create your views here.

# 查询全部

def Find_Star_Photos(request):
    Star_Info = Star_photos.objects.all()
    return Star_Info
