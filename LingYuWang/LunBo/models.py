from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.

# 轮播图

class LunBo(models.Model):
    LunBo_title = models.CharField(u'标题', max_length=30)
    LunBo_URL = models.ImageField(u'图片', upload_to='LunBo')
    LunBo_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.LunBo_title

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
