from django.urls import path
from LunBo.views import *

app_name = 'l2'


urlpatterns = [
    path('LunBo/', Lun_Bo, name='LunBo'),
]
