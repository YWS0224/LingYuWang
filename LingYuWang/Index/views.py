from django.shortcuts import render
from LunBo.views import *


# Create your views here.

def Index_html(request):
    LunBo_T = Lun_Bo(request)
    return render(request, 'Index2.html', {'LunBo_T': LunBo_T})

#
# def dash(request):
#     return render(request, 'Index.html')
