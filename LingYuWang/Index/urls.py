from django.urls import path, include, re_path
from .views import *

from Index import views


app_name = 'Index'


urlpatterns = [
    path('index/', Index_html, name='index'),
    path('Movie/', Movie, name='Movie'),
    path('Tv/', Tv, name='Tv'),
    path('Star/', Star, name='Star'),
    re_path(r'^Ding/(\d{1,2})/', San, name='Ding')
    # re_path(r'^index2(\d{1,2})', views, dash, name='index2'),
]
