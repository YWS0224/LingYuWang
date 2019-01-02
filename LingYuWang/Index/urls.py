from django.urls import path, re_path
from .views import *

from Index import views


app_name = 'Index'


urlpatterns = [
    path('index/', Index_html, name='index'),
    # re_path(r'^index2(\d{1,2})', views, dash, name='index2'),
]
