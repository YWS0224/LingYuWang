from django.contrib import admin
import xadmin
from Movie_column.models import *


#
# # Register your models here.
#
@xadmin.sites.register(Movie)
class Movie_column_admin(object):
    list_display = ('id', 'Movie_Title', 'Movie_Info', 'img_url')
    list_display_links = ('id', 'Movie_Title')
    model_icon = 'fa'
    style_fields = {"Movie_Info": "ueditor"}
