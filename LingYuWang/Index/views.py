from django.shortcuts import render
from LunBo.views import *
from Welfare.views import *
from JuKaLaiLe.views import *
from Star_Photos.views import *
from Movie_column.views import *
from TV_Play.views import *
from Star.views import *

# Create your views here.

def Index_html(request):
    LunBo_T = Lun_Bo(request)
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Movie = select_Movie(request)
    Movie_xd = select_Movie_Xiaode(request)
    return render(request, 'Index2.html', {'LunBo_T': LunBo_T,
                                           'Welfare_T': Welfare_T,
                                           'Jukalaile': Jukalaile,
                                           'Star_Phtos': Starphotos,
                                           'Movie': Movie,
                                           'Movie_xd': Movie_xd})

def Index3_html(request):
    LunBo_T = Lun_Bo(request)
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    selectMovie = select_Movie(request)
    TvPlay = Tv_play(request)
    Star1 = Find_Star(request)
    return render(request, 'Index3.html', {'LunBo_T': LunBo_T,
                                           'Welfare_T': Welfare_T,
                                           'Jukalaile': Jukalaile,
                                           'Star_Phtos': Starphotos,
                                           'select_Movie': selectMovie,
                                           'Tv_Play1': TvPlay,
                                           'Star1': Star1,
                                           })

#
# def dash(request):
#     return render(request, 'Index.html')
