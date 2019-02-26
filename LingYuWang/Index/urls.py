from django.urls import path, include, re_path
from .views import *

from Index import views


app_name = 'Index'


urlpatterns = [
    path('index/', Index_html, name='index'),
    path('Movie/', Movie, name='Movie'),
    path('Tv/', Tv, name='Tv'),
    path('Star/', Star, name='Star'),
    path('ZiXun/', ZiXun, name='Zixun'),
    re_path(r'^ZhuanFang/(\d{1,2})/', ZhuanF, name='ZhuanFangInfo'),
    re_path(r'^Tv/(\d{1,2})/', Tv_San, name='Tvinfo'),
    re_path(r'^Star/(\d{1,2})/', Star_San, name='Star_info'),
    re_path(r'^Ding/(\d{1,2})/', San, name='Ding'),
    re_path(r'^CeHua/(\d{1,2})/', CeHua, name='CeHuaInfo'),
    re_path(r'^YingPingShe/(\d{1,2})/', YingPingShe_SanJi, name='YingPingShe'),
    re_path(r'^Welfare/(\d{1,2})/', Welfare_SanJi, name='Welfare'),
    re_path(r'^JuKaLaiL/(\d{1,2})/', JuKaLaiLe_SanJi, name='JuKa'),

]
