from django.shortcuts import render
from .models import *

# Create your views here.


def select_Movie(request):
    MList = Movie.objects.all()
    return MList


def uploadImg(request):
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('Movie'))
        img.save()
    return render(request, 'Index.html')
