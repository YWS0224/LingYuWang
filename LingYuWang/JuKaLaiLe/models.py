from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class Jukalai_L(models.Model):
    Jukalail_title = models.CharField(u'标题', max_length=30)
    Jukalail_title_xd = models.CharField(u'小标题', max_length=30, default='')
    Jukalail_title_Keyword = models.CharField(u'关键词', max_length=30, default='')
    Jukalail_UserName = models.CharField(u'编辑名称', max_length=30, default='')
    Jukalail_Index = models.IntegerField(u'排序', default=2)
    Jukalail_URL = models.ImageField(u'图片', upload_to='JuKaLaiLe', blank=True)
    Jukalail_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Jukalail_title

    class Meta:
        verbose_name = "剧咖来了"
        verbose_name_plural = verbose_name
