from django.db import models


# Create your models here.

#  福利社

class Find_welfare_Info(models.Model):
    Welfare_Title = models.CharField(u'标题', max_length=30)
    Walfare_Url = models.ImageField(u'图片', upload_to='Welfare')
    Walfare_Info = models.CharField(u'内容', max_length=50)

    def __str__(self):
        return self.Welfare_Title

    class Meta:
        verbose_name = "福利社"
        verbose_name_plural = verbose_name
