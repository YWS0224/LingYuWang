from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class CeHua_photos(models.Model):
    CeHua_url = models.ImageField(u'图片', upload_to='Movie', blank=True)
    CeHua_Title = models.CharField(u'标题', max_length=30)
    CeHuaTitle_xd = models.CharField(u'小标题', max_length=30, default='')
    CeHua_Title_Keyword = models.CharField(u'关键字', max_length=30, default='')
    CeHua_UserName = models.CharField(u'编辑名称', max_length=30, default='')
    CeHua_Type = models.CharField(u'分类', max_length=30, default='')
    CeHua_LaiYuan = models.CharField(u'来源', max_length=30, default='')
    CeHua_RiQi = models.DateField(u'发布日期', auto_now_add=True)
    CeHua_Index = models.IntegerField(u'排序', default=2)
    CeHua_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                              filePath="courses/ueditor/", default='')
    def __str__(self):
        return self.CeHua_Title

    class Meta:
        verbose_name = "策划"
        verbose_name_plural = verbose_name
