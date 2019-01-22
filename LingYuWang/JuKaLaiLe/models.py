from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class Jukalai_L(models.Model):
    Jukalail_title = models.CharField(u'标题', max_length=30)
    Jukalail_URL = models.ImageField(u'图片', upload_to='JuKaLaiLe')
    Jukalail_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Jukalail_title

    class Meta:
        verbose_name = "剧咖来了大"
        verbose_name_plural = verbose_name


class Jukalai_L_Xd(models.Model):
    Jukalail_title = models.CharField(u'标题', max_length=30)
    Jukalail_URL = models.ImageField(u'图片', upload_to='JuKaLaiLe')
    Jukalail_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Jukalail_title

    class Meta:
        verbose_name = "剧咖来了小"
        verbose_name_plural = verbose_name


