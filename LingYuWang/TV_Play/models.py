from django.db import models

# Create your models here.
class Tv_Play(models.Model):
    Tv_Title = models.CharField(u'标题', max_length=30)
    Tv_Url = models.ImageField(u'图片', upload_to='TV_Play')
    Tv_Info = models.CharField(u'内容', max_length=50)

    def __str__(self):
        return self.Tv_Title

    class Meta:
        verbose_name = "电视剧"
        verbose_name_plural = verbose_name
