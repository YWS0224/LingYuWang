from django.db import models


# Create your models here.

# 轮播图

class LunBo(models.Model):
    LunBo_title = models.CharField(u'标题', max_length=30)
    LunBo_URL = models.ImageField(u'图片', upload_to='LunBo')
    LunBo_Info = models.CharField(u'内容', max_length=50)

    def __str__(self):
        return self.LunBo_title

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
