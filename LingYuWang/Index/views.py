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


# 总
def Index_html(request):
    LunBo_List = Lun_Bo(request)
    Lun_first = Lun_Bo_First(request)

    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)

    Movie_list = select_Movie(request)
    Movie_first = select_Movie_first(request)

    Star_List = Find_Star(request)
    Star_first = Find_Star_first(request)

    Tv_list = Tv_play(request)
    Tv_First = Tv_first(request)

    Yingpin = Yingping_Star_Info(request)

    return render(request, 'Index.html', {
                                           'LunBo_list': LunBo_List,
                                           'Lun_first': Lun_first,

                                           'Welfare_T': Welfare_T,
                                           'Jukalaile': Jukalaile,
                                           'Star_Phtos': Starphotos,

                                           'Movie_list': Movie_list,
                                           'Movie_first': Movie_first,

                                           'Star_list': Star_List,
                                           'Star_first': Star_first,


                                           'Tv_list': Tv_list,
                                           'Tv_first': Tv_First,

                                           'Yingpingshe': Yingpin,
                                           })


# 电影
def Movie(request):
    Movie_all = select_all(request)
    return render(request, 'Movie.html', {'Movie_all': Movie_all})


# 电视剧
def Tv(request):
    Tv_all_list = Tv_all(request)
    return render(request, 'Tv.html', {'Tv_all': Tv_all_list})


# 明星
def Star(request):
    Star_all = Find_All(request)
    return render(request, 'Star.html', {'Star_all': Star_all})



def San(request):
    LunBo_T = Lun_Bo(request)
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Movie = select_Movie(request)
    Star_Title = Find_Star(request)
    Tv = Tv_play(request)
    Yingpin = Yingping_Star_Info(request)
    return render(request, 'Sanji.html', {'LunBo_T': LunBo_T,
                                           'Welfare_T': Welfare_T,
                                           'Jukalaile': Jukalaile,
                                           'Star_Phtos': Starphotos,
                                           'Movie': Movie,
                                           'Star_Title1': Star_Title,
                                          'Tv_Title': Tv,
                                          'Yingpingshe': Yingpin,
                                          })


