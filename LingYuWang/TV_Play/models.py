from django.db import models

# Create your models here.
class Tv_Play(models.Model):
    Tv_Title = models.CharField(max_length=30)
    Tv_Url = models.ImageField(upload_to='img')
    Tv_Info = models.CharField(max_length=50)