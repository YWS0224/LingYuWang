from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class Find_Star_Info(models.Model):
    Star_Title = models.CharField(u'标题', max_length=30)
    Star_Title_xd = models.CharField(u'小标题', max_length=30, default='')
    Star_Title_Keyword = models.CharField(u'关键词', max_length=30, default='')
    Star_UserName = models.CharField(u'编辑名称', max_length=30, default='')
    Star_Index = models.IntegerField(u'排序', default=2)
    Star_Url = models.ImageField(u'图片', upload_to='Star', blank=True)
    Star_Type = models.CharField(u'分类', max_length=30, default='')
    Star_LaiY = models.CharField(u'来源', max_length=30, default='')
    Star_RiQi = models.DateField(u'发布日期', auto_now_add=True)
    Star_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Star_Title

    class Meta:
        verbose_name = "明星"
        verbose_name_plural = verbose_name
