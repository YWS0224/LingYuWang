import xadmin
from JuKaLaiLe.models import *
# Register your models here.

@xadmin.sites.register(Jukalai_L)
class Jukalai_L_admin(object):
    list_display = ('id', 'Jukalail_title', 'Jukalail_Info', 'Jukalail_URL')
    list_display_links = ('id', 'Jukalaile_title')
    model_icon = 'fa'
    style_fields = {"Jukalail_Info": "ueditor"}
