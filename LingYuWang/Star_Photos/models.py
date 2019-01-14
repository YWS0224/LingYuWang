from django.db import models

# Create your models here.
class Star_photos(models.Model):
    Star_Title = models.CharField(u'标题', max_length=30)
    Star_Url = models.ImageField(u'图片', upload_to='Star_Photos')
    Star_Info = models.CharField(u'内容', max_length=50)

    def __str__(self):
        return self.Star_Title

    class Meta:
        verbose_name = "明星美图"
        verbose_name_plural = verbose_name
