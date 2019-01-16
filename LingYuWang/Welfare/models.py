from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.

#  福利社

class Find_welfare_Info(models.Model):
    Welfare_Title = models.CharField(u'标题', max_length=30)
    Walfare_Url = models.ImageField(u'图片', upload_to='Welfare')
    Walfare_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Welfare_Title

    class Meta:
        verbose_name = "福利社"
        verbose_name_plural = verbose_name
