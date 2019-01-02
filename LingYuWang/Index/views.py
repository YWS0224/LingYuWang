from django.shortcuts import render
from LunBo.views import *
from topType.views import *


# Create your views here.

def Index_html(request):
    LunBo_T = Lun_Bo(request)
    top_Type1 = top_Type(request)
    return render(request, 'Index.html', {'LunBo_T': LunBo_T, 'TopType': top_Type1})

#
# def dash(request):
#     return render(request, 'Index.html')
