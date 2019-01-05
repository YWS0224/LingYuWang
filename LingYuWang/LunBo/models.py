from django.db import models


# Create your models here.

# 轮播图

class LunBo(models.Model):
    LunBo_title = models.CharField(max_length=30)
    LunBo_URL = models.ImageField(upload_to='img')
    LunBo_Info = models.CharField(max_length=50)
