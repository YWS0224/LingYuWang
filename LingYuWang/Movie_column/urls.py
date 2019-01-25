from django.urls import path, include, re_path
from .views import *

app_name = 'Movie'

urlpatterns = [
    re_path(r'^Movie/(\d{1,5})/', select_Movie_ById, name='Movie'),

]
