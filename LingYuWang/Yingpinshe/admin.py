
import xadmin
from Yingpinshe.views import *
# Register your models here.


@xadmin.sites.register(Yingping_Star_Info)
class Find_Star_Info_admin(object):
    list_display = ('id', 'Yingping_Title', 'Yingping_Info', 'Yingping_Url')
    list_display_links = ('id', 'Yingping_Title')
    model_icon = 'fa'
    style_fields = {"Yingping_Info": "ueditor"}


@xadmin.sites.register(Yingping_Star_Info_xd)
class Find_Star_Info_admin_Xd(object):
    list_display = ('id', 'Yingping_Title', 'Yingping_Info', 'Yingping_Url')
    list_display_links = ('id', 'Yingping_Title')
    model_icon = 'fa'
    style_fields = {"Yingping_Info": "ueditor"}
