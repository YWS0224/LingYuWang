import xadmin
from TV_Play.models import *
# Register your models here.


@xadmin.sites.register(Tv_Play)
class Tv_Play_admin(object):
    list_display = ('id', 'Tv_Title', 'Tv_Info', 'Tv_Url')
    list_display_links = ('id', 'Tv_Title')
    model_icon = 'fa'
    style_fields = {"Tv_Info": "ueditor"}


@xadmin.sites.register(Tv_Play_xd)
class Tv_Play_admin_xd(object):
    list_display = ('id', 'Tv_Title', 'Tv_Info', 'Tv_Url')
    list_display_links = ('id', 'Tv_Title')
    model_icon = 'fa'
    style_fields = {"Tv_Info": "ueditor"}
