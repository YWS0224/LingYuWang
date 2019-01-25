from django.urls import path, include, re_path
from .views import *

app_name = 'Star'

urlpatterns = [
    re_path(r'^Star/(\d{1,5})/', Find_Star_ById, name='Star'),

]
