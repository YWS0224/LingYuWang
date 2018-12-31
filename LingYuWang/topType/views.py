from django.shortcuts import render
from topType.models import *


# Create your views here.
def top_Type(request):
    TopType1 = Top_Type.objects.all()
    return render(request, 'Index.html', {'TopType': TopType1})
