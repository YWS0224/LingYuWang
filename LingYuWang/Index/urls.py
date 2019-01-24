from django.urls import path, include
from .views import *

from Index import views


app_name = 'Index'


urlpatterns = [
    path('index/', Index_html, name='index'),
    path('index3/', Movie, name='Movie'),
    path('Tv/', Tv, name='Tv'),
    path('Star/', Star, name='Star'),
    path('Ding/', San, name='Ding')
    # re_path(r'^index2(\d{1,2})', views, dash, name='index2'),
]
