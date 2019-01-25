from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Movie(models.Model):
    img_url = models.ImageField(u'图片', upload_to='Movie', blank=True)
    Movie_Title = models.CharField(u'标题', max_length=30)
    Movie_Title_xd = models.CharField(u'小标题', max_length=30, default='')
    Movie_Title_Keyword = models.CharField(u'关键字', max_length=30, default='')
    Movie_UserName = models.CharField(u'编辑名称', max_length=30, default='')
    Movie_Index = models.IntegerField(u'排序', default=2)
    Movie_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Movie_Title

    class Meta:
        verbose_name = "电影"
        verbose_name_plural = verbose_name
