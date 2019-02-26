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
    JuKa_first = JuKaiLaiLe_first(request)
    Starphotos = Find_Star_Photos(request)
    Yingping = Yingping_find_all(request)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)


    Movie_list = select_Movie(request)
    Movie_first = select_Movie_first(request)
    Star_List = Find_Star(request)
    Star_first = Find_Star_first(request)
    Tv_list = Tv_play(request)
    Tv_First = Tv_first(request)
    return render(request, 'Index.html', {
        'LunBo_list': LunBo_List,
        'Lun_first': Lun_first,
        'Welfare_T': Welfare_T,
        'Jukalaile': Jukalaile,
        'JuKa_first': JuKa_first,
        'Star_Phtos': Starphotos,
        'Yingpingshe': Yingping,
        'ZhuanF': ZhuangF,
        'CeHua': CeHua_List,

        'Movie_list': Movie_list,
        'Movie_first': Movie_first,

        'Star_list': Star_List,
        'Star_first': Star_first,
        'Tv_list': Tv_list,
        'Tv_first': Tv_First,


    })


# 电影二级
def Movie(request):
    Movie_all = select_all(request)
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Yingping = Yingping_find_all(request)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)
    return render(request, 'Movie.html', {'Movie_all': Movie_all,
                                          'Welfare_T': Welfare_T,
                                          'Jukalaile': Jukalaile,
                                          'Star_Phtos': Starphotos,
                                          'Yingpingshe': Yingping,
                                          'ZhuanF': ZhuangF,
                                          'CeHua': CeHua_List,
                                          })


# 根据电视剧id 查询电影信息
def Tv(request):
    Tv_all_list = Tv_all(request)
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Yingping = Yingping_find_all(request)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)
    return render(request, 'Tv.html', {'Tv_all': Tv_all_list,
                                       'Welfare_T': Welfare_T,
                                       'Jukalaile': Jukalaile,
                                       'Star_Phtos': Starphotos,
                                       'Yingpingshe': Yingping,
                                       'ZhuanF': ZhuangF,
                                       'CeHua': CeHua_List,
                                       })


# 明星二级页面
def Star(request):
    Star_all = Find_All(request)
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Yingping = Yingping_find_all(request)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)
    return render(request, 'Star.html', {'Star_all': Star_all,
                                         'Welfare_T': Welfare_T,
                                         'Jukalaile': Jukalaile,
                                         'Star_Phtos': Starphotos,
                                         'Yingpingshe': Yingping,
                                         'ZhuanF': ZhuangF,
                                         'CeHua': CeHua_List,
                                         })


# 独家专访三级
def ZhuanF(request, Zid):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Yingping = Yingping_find_all(request)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)
    ZF = Find_ZhuanFang_ByID(request, Zid)

    return render(request, "ZhuanFang_Sanji.html", {'ZF': ZF,
                                                    'Welfare_T': Welfare_T,
                                                    'Jukalaile': Jukalaile,
                                                    'Star_Phtos': Starphotos,
                                                    'Yingpingshe': Yingping,
                                                    'ZhuanF': ZhuangF,
                                                    'CeHua': CeHua_List,
                                                    })


# 策划三级
def CeHua(request, Cid):
    CH = Find_CeHua_ByID(request, Cid)
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Yingping = Yingping_find_all(request)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)
    return render(request, 'CeHua_Sanji.html', {'CH': CH,
                                                'CeHua_List': CeHua_List,
                                                'Welfare_T': Welfare_T,
                                                'Jukalaile': Jukalaile,
                                                'Star_Phtos': Starphotos,
                                                'Yingpingshe': Yingping,
                                                'ZhuanF': ZhuangF,
                                                'CeHua': CeHua_List,
                                                })


# 电影三级
def San(request, mid):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Movie = select_Movie(request)
    Movie_all = select_all(request)
    Star_Title = Find_Star(request)
    Tv = Tv_play(request)
    Yingpin = Yingping_find_all(request)
    Movie_Info = select_Movie_ById(request, mid)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)
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
        'ZhuanF': ZhuangF,
        'CeHua': CeHua_List,
    })


# 电视剧三级
def Tv_San(request, Tid):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Movie = select_Movie(request)
    Star_Title = Find_Star(request)
    Tv = Tv_play(request)
    Yingpin = Yingping_find_all(request)
    Tv_Biao = Tv_ById(request, Tid)
    Tv_all_list = Tv_all(request)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)
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
        'ZhuanF': ZhuangF,
        'CeHua': CeHua_List,
    })


# 明星三级
def Star_San(request, Sid):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Movie = select_Movie(request)
    Star_Title = Find_Star(request)
    Tv = Tv_play(request)
    Yingpin = Yingping_find_all(request)
    Star = Find_Star_ById(request, Sid)
    Star_all = Find_All(request)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)
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
        'ZhuanF': ZhuangF,
        'CeHua': CeHua_List,
    })


# 资讯二级页面
def ZiXun(request):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Yingpin = Yingping_find_all(request)
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


# 影评社三级页面
def YingPingShe_SanJi(request, Yid):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Star_Title = Find_Star(request)
    Yingpin = Yingping_find_all(request)
    YingPing_ById = YingPing_Byid(request, Yid)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)
    return render(request, 'YingPingShe_Sanji.html', {
        'Welfare_T': Welfare_T,
        'Jukalaile': Jukalaile,
        'Star_Phtos': Starphotos,
        'Star_Title1': Star_Title,
        'Yingpingshe': Yingpin,
        'YingPing_ById': YingPing_ById,
        'ZhuanF': ZhuangF,
        'CeHua': CeHua_List,
    })


# 福利社三级页面
def Welfare_SanJi(request, Wid):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Star_Title = Find_Star(request)
    Welfare_info = Welfare_Byid(request, Wid)
    Yingping = Yingping_find_all(request)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)
    return render(request, 'FuLiShe_Sanji.html', {
        'Welfare_T': Welfare_T,
        'Jukalaile': Jukalaile,
        'Star_Phtos': Starphotos,
        'Star_Title1': Star_Title,
        'Welfare_info': Welfare_info,
        'Yingpingshe': Yingping,
        'ZhuanF': ZhuangF,
        'CeHua': CeHua_List,
    })


# 剧咖来了三级页面
def JuKaLaiLe_SanJi(request, Jid):
    Welfare_T = Find_Welfare(request)
    Jukalaile = Jukalaile_find_all(request)
    Starphotos = Find_Star_Photos(request)
    Star_Title = Find_Star(request)
    Yingping = Yingping_find_all(request)
    ZhuangF = select_ZhuanFang(request)
    CeHua_List = select_CeHua(request)
    JuKa_Info = JuKaLaiLe_ById(request, Jid)
    return render(request, 'JuKaLaiLe_Sanji.html', {
        'Welfare_T': Welfare_T,
        'Jukalaile': Jukalaile,
        'Star_Phtos': Starphotos,
        'Star_Title1': Star_Title,
        'JuKa_Info': JuKa_Info,
        'Yingpingshe': Yingping,
        'ZhuanF': ZhuangF,
        'CeHua': CeHua_List,
    })
