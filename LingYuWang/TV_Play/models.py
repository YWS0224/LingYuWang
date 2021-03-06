from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Tv_Play(models.Model):
    Tv_Title = models.CharField(u'标题', max_length=30)
    Tv_Title_xd = models.CharField(u'小标题', max_length=30, default='')
    Tv_Title_Keyword = models.CharField(u'关键词', max_length=30, default='')
    TV_UserName = models.CharField(u'编辑名称', max_length=30, default='')
    TV_Index = models.IntegerField(u'排序', default=2)
    Tv_Url = models.ImageField(u'图片', upload_to='TV_Play', blank=True)
    Tv_Type = models.CharField(u'分类', max_length=30, default='')
    Ty_LaiY = models.CharField(u'来源', max_length=30, default='')
    Ty_RiQi = models.DateField(u'发布日期', auto_now_add=True)
    Tv_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Tv_Title

    class Meta:
        verbose_name = "电视剧"
        verbose_name_plural = verbose_name
