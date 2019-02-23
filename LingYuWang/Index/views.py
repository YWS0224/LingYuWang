from django.shortcuts import render
from LunBo.views import *
from Welfare.views import *
from JuKaLaiLe.views import *
from Star_Photos.views import *
from Movie_column.views import *
from TV_Play.views import *
from Star.views import *
from Yingpinshe.views import *
from ZhuanFang.views import *
from CeHua.views import *
# Create your views here.


# 首页
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

    ZhuangF = select_ZhuanFang(request)

    CeHua_List = select_CeHua(request)
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

                                            'ZhuanF': ZhuangF,
        
                                            'CeHua': CeHua_List,
                                           })


# 电影
def Movie(request):
    Movie_all = select_all(request)
    return render(request, 'Movie.html', {'Movie_all': Movie_all})


# 根据电影id 查询电影信息
def MovieId(request, id):
    Movie_Info = select_Movie_ById(request, id)
    return render(request, 'Movie_Sanji.html', {'Movie_Info': Movie_Info})


# 电视剧
def Tv(request):
    Tv_all_list = Tv_all(request)
    return render(request, 'Tv.html', {'Tv_all': Tv_all_list})


# 明星
def Star(request):
    Star_all = Find_All(request)
    return render(request, 'Star.html', {'Star_all': Star_all})


# 独家专访三级
def ZhuanF(request, Zid):
    ZF = Find_ZhuanFang_ByID(request, Zid)
    ZhuangF = select_ZhuanFang(request)
    return render(request, "ZhuanFang_Sanji.html", {'ZF': ZF,
                                                    'ZhuanF': ZhuangF})

# 策划三级
def CeHua(request, Cid):
    CH = Find_CeHua_ByID(request, Cid)
    CeHua_List = select_CeHua(request)
    return render(request, 'CeHua_Sanji.html', {'CH': CH,
                                                'CeHua_List': CeHua_List})


# 电影三级
def San(request, mid):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Movie = select_Movie(request)
    Movie_all = select_all(request)
    Star_Title = Find_Star(request)
    Tv = Tv_play(request)
    Yingpin = Yingping_Star_Info(request)
    Movie_Info = select_Movie_ById(request, mid)
    return render(request, 'Movie_Sanji.html', {
                                           'Welfare_T': Welfare_T,
                                           'Jukalaile': Jukalaile,
                                           'Star_Phtos': Starphotos,
                                           'Movie': Movie,
                                           'Star_Title1': Star_Title,
                                           'Tv_Title': Tv,
                                           'Yingpingshe': Yingpin,
                                           'Movie_Info': Movie_Info,
                                           'Movie_all': Movie_all,
                                          })

# 电视剧三级
def Tv_San(request, Tid):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Movie = select_Movie(request)
    Star_Title = Find_Star(request)
    Tv = Tv_play(request)
    Yingpin = Yingping_Star_Info(request)
    Tv_Biao = Tv_ById(request, Tid)
    Tv_all_list = Tv_all(request)
    return render(request, 'TV_Sanji.html', {
                                            'Welfare_T': Welfare_T,
                                            'Jukalaile': Jukalaile,
                                            'Star_Phtos': Starphotos,
                                            'Movie': Movie,
                                            'Star_Title1': Star_Title,
                                            'Tv_Title': Tv,
                                            'Yingpingshe': Yingpin,
                                            'Tv_Biao': Tv_Biao,
                                            'Tv_all': Tv_all_list,
                                            })


# 明星三级
def Star_San(request, Sid):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Movie = select_Movie(request)
    Star_Title = Find_Star(request)
    Tv = Tv_play(request)
    Yingpin = Yingping_Star_Info(request)
    Star = Find_Star_ById(request, Sid)
    Star_all = Find_All(request)
    return render(request, 'Star_Sanji.html', {
                                            'Welfare_T': Welfare_T,
                                            'Jukalaile': Jukalaile,
                                            'Star_Phtos': Starphotos,
                                            'Movie': Movie,
                                            'Star_Title1': Star_Title,
                                            'Tv_Title': Tv,
                                            'Yingpingshe': Yingpin,
                                            'Star': Star,
                                            'Star_all': Star_all,
                                            })


# 资讯
def ZiXun(request):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Yingpin = Yingping_Star_Info(request)
    Star_all = Find_All(request)
    Movie_all = select_all(request)
    Tv_all_list = Tv_all(request)
    return render(request, 'ZiXun.html', {
                                            'Welfare_T': Welfare_T,
                                            'Jukalaile': Jukalaile,
                                            'Star_Phtos': Starphotos,
                                            'Yingpingshe': Yingpin,
                                            'Star_all': Star_all,
                                            'Movie_all': Movie_all,
                                            'Tv_all_list': Tv_all_list,
                                        })
