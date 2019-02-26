from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.

#  福利社

class Find_welfare_Info(models.Model):
    Welfare_Title = models.CharField(u'标题', max_length=30)
    Welfare_Title_xd = models.CharField(u'小标题', max_length=30, default='')
    Welfare_Title_Keyword = models.CharField(u'关键词', max_length=30, default='')
    Welfare_UserName = models.CharField(u'编辑名称', max_length=30, default='')
    Welfare_Index = models.IntegerField(u'排序', default=2)
    Welfare_Type = models.CharField(u'分类', max_length=30, default='')
    Welfare_LaiYuan = models.CharField(u'来源', max_length=30, default='')
    Welfare_RiQi = models.DateField(u'发布日期', auto_now_add=True)
    Walfare_Url = models.ImageField(u'图片', upload_to='Welfare', blank=True)
    Walfare_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.Welfare_Title

    class Meta:
        verbose_name = "福利社"
        verbose_name_plural = verbose_name
