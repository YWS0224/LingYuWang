from django.urls import path, include, re_path
from .views import *

app_name = 'Tv'

urlpatterns = [
    re_path(r'^Tv/(\d{1,5})/', Tv_ById, name='Tv'),

]
