from django.db import models

# Create your models here.
class Find_Star_Info(models.Model):
    Star_Title = models.CharField(max_length=30)
    Star_Url = models.ImageField(upload_to='img')
    Star_Info = models.CharField(max_length=50)