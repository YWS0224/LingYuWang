from django.db import models

# Create your models here.


# 顶部分类
class Top_Type(models.Model):
    TopType = models.CharField(max_length=30)

