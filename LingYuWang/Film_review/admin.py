import xadmin
from Film_review.models import *
# Register your models here.

@xadmin.sites.register(film_review)
class Film_review_admin(object):
    list_display = ('id', 'f_Title', 'f_Info', 'f_URL')
    list_display_links = ('id', 'f_Title')

