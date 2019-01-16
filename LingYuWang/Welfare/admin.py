import xadmin
from Welfare.models import *
# Register your models here.


@xadmin.sites.register(Find_welfare_Info)
class Find_welfare_Info_admin(object):
    list_display = ('id', 'Welfare_Title', 'Walfare_Info', 'Walfare_Url')
    list_display_links = ('id', 'Welfare_Title')
    model_icon = 'fa'
    style_fields = {"Walfare_Info": "ueditor"}
