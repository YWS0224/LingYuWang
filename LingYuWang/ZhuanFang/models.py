from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.

class Find_ZhuanFang(models.Model):
    ZhuanFang_Title = models.CharField(u'标题', max_length=30)
    ZhuanFang_Url = models.ImageField(u'图片', upload_to='ZhuanFang', blank=True)
    ZhuanFang_sTitle = models.CharField(u'小标题', max_length=50, default='')
    ZhuanFang_Keyword = models.CharField(u'关键词', max_length=50, default='')
    ZhuanFang_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')


    def __str__(self):
        return self.ZhuanFang_Title

    class Meta:
        verbose_name = '专访大'
        verbose_name_plural = verbose_name


class Find_ZhuanFang_XD(models.Model):
    ZhuanFang_Title = models.CharField(u'标题', max_length=30)
    ZhuanFang_Url = models.ImageField(u'图片', upload_to='ZhuanFang', blank=True)
    ZhuanFang_sTitle = models.CharField(u'小标题', max_length=50, default='')
    ZhuanFang_Keyword = models.CharField(u'关键词', max_length=50, default='')
    ZhuanFang_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')


    def __str__(self):
        return self.ZhuanFang_Title

    class Meta:
        verbose_name = '专访小'
        verbose_name_plural = verbose_name


