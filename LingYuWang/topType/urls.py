from django.urls import path
from topType.views import *

app_name = 'l1'

urlpatterns = [
    path('topType/', top_Type, name='top_Type'),
]
