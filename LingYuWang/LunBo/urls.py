from django.urls import path, include, re_path
from .views import *

app_name = 'LunBo'

urlpatterns = [
    re_path(r'^LunBo/(\d{1,5})/', LunBo_ById, name='Movie'),

]
