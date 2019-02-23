from django.contrib import admin
import xadmin
from CeHua.models import *

# Register your models here.
@xadmin.sites.register(CeHua_photos)
class CeHua_admin(object):
    list_display = ('id', 'CeHua_Title', 'CeHua_Title_Keyword', 'CeHua_Info')
    list_display_links = ('id', 'CeHua_Title')
    model_icon = 'fa'
    style_fields = {"CeHua_Info": "ueditor"}
