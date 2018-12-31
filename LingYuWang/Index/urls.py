from django.urls import path
from .views import *

app_name = 'Index'

urlpatterns = [
    path('index/', Index_html, name='index'),
]
