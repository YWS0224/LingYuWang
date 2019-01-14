import xadmin
from LunBo.models import *
# Register your models here.


@xadmin.sites.register(LunBo)
class LunBo_admin(object):
    list_display = ('id', 'LunBo_title', 'LunBo_Info', 'LunBo_URL')
    list_display_links = ('id', 'LunBo_title')
    model_icon = 'fa'
