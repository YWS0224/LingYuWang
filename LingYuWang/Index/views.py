from django.shortcuts import render
from LunBo.views import *
from Welfare.views import *
from JuKaLaiLe.views import *
from Star_Photos.views import *
from Movie_column.views import *
from TV_Play.views import *
from Star.views import *
from Yingpinshe.views import *
# Create your views here.

def Index_html(request):
    LunBo_T = Lun_Bo(request)
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Movie = select_Movie(request)
    Movie_xd = select_Movie_Xiaode(request)
    Star_Title = Find_Star(request)
    Star_Title_xd = Find_Star_xd(request)
    Tv = Tv_play(request)
    Tv_xd = Tv_play_xd(request)
    Yingpin = Yingping_Star_Info(request)
    Yingpin_xd = Yingping_find_all_Xd(request)
    return render(request, 'Index2.html', {'LunBo_T': LunBo_T,
                                           'Welfare_T': Welfare_T,
                                           'Jukalaile': Jukalaile,
                                           'Star_Phtos': Starphotos,
                                           'Movie': Movie,
                                           'Movie_xd': Movie_xd,
                                           'Star_Title1': Star_Title,
                                           'Star_xd': Star_Title_xd,
                                           'Tv_Title': Tv,
                                           'Tv_Title_xd': Tv_xd,
                                           'Yingpingshe': Yingpin,
                                           'Yingpingshe_Xd': Yingpin_xd,
                                           })


#
# def dash(request):
#     return render(request, 'Index.html')
