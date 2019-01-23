from django.db import models
# Create your models here.
from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class Yingping_Star_Info(models.Model):
    Yingping_Title = models.CharField(u'标题', max_length=30)
    Yingping_Url = models.ImageField(u'图片', upload_to='Yingping')
    Yingping_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Yingping_Title

    class Meta:
        verbose_name = "影评社大"
        verbose_name_plural = verbose_name


class Yingping_Star_Info_xd(models.Model):
    Yingping_Title = models.CharField(u'标题', max_length=30)
    Yingping_Url = models.ImageField(u'图片', upload_to='Yingping')
    Yingping_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Yingping_Title

    class Meta:
        verbose_name = "影评社小"
        verbose_name_plural = verbose_name
