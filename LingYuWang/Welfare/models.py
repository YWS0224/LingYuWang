from django.db import models


# Create your models here.

#  福利社

class Find_welfare_Info(models.Model):
    Welfare_Title = models.CharField(max_length=30)
    Walfare_Url = models.ImageField(upload_to='img')
    Walfare_Info = models.CharField(max_length=50)
