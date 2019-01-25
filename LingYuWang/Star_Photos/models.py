from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Star_photos(models.Model):
    Star_Title = models.CharField(u'标题', max_length=30)
    Star_Title_Keyword = models.CharField(u'关键词', max_length=30, default='')
    Star_UserName = models.CharField(u'编辑名称', max_length=30, default='')
    Star_Index = models.IntegerField(u'排序', default=2)
    Star_Url = models.ImageField(u'图片', upload_to='Star_Photos', blank=True)
    Star_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Star_Title

    class Meta:
        verbose_name = "明星美图"
        verbose_name_plural = verbose_name
