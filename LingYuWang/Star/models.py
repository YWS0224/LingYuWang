from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class Find_Star_Info(models.Model):
    Star_Title = models.CharField(u'标题', max_length=30)
    Star_Url = models.ImageField(u'图片', upload_to='Star')
    Star_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Star_Title

    class Meta:
        verbose_name = "明星"
        verbose_name_plural = verbose_name
