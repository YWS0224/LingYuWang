import xadmin
from Star_Photos.models import *
# Register your models here.


@xadmin.sites.register(Star_photos)
class Star_photos_admin(object):
    list_display = ('id', 'Star_Title', 'Star_Info', 'Star_Url')
    list_display_links = ('id', 'Star_Title')
    model_icon = 'fa'
