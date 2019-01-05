from django.shortcuts import render
from Welfare.models import *


# Create your views here.
def Find_Welfare(request):
    w_info = Find_welfare_Info.objects.all()
    return w_info


