import xadmin
from .models import *
# Register your models here.


@xadmin.sites.register(Find_ZhuanFang)
class ZhuanFang_admin(object):
    list_display = ('id', 'ZhuanFang_Title', 'ZhuanFang_Info', 'ZhuanFang_Url', 'ZhuanFang_sTitle')
    list_display_links = ('id', 'Movie_Title')
    model_icon = 'fa'
    style_fields = {"ZhuanFang_Info": "ueditor"}


@xadmin.sites.register(Find_ZhuanFang_XD)
class ZhuanFang_admin(object):
    list_display = ('id', 'ZhuanFang_Title', 'ZhuanFang_Info', 'ZhuanFang_Url', 'ZhuanFang_sTitle')
    list_display_links = ('id', 'Movie_Title')
    model_icon = 'fa'
    style_fields = {"ZhuanFang_Info": "ueditor"}
