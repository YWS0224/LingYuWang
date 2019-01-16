from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Movie(models.Model):
    img_url = models.ImageField(u'图片', upload_to='Movie')
    Movie_Title = models.CharField(u'标题', max_length=30)
    Movie_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Movie_Title

    class Meta:
        verbose_name = "电影大"
        verbose_name_plural = verbose_name


class Movie_xiaode(models.Model):
    img_url = models.ImageField(u'图片', upload_to='Movie')
    Movie_Title = models.CharField(u'标题', max_length=30)
    Movie_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Movie_Title

    class Meta:
        verbose_name = "电影小"
        verbose_name_plural = verbose_name
