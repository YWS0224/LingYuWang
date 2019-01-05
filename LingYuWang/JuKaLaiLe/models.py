from django.db import models

# Create your models here.
class Jukalai_L(models.Model):
    Jukalail_title = models.CharField(max_length=30)
    Jukalail_URL = models.ImageField(upload_to='img')
    Jukalail_Info = models.CharField(max_length=50)