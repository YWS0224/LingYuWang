import xadmin
from Star.models import *
# Register your models here.


@xadmin.sites.register(Find_Star_Info)
class Find_Star_Info_admin(object):
    list_display = ('id', 'Star_Title', 'Star_Info', 'Star_Url')
    list_display_links = ('id', 'Star_Title')
    model_icon = 'fa'
