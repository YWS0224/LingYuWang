from django.db import models

# Create your models here.
class Jukalai_L(models.Model):
    Jukalail_title = models.CharField(u'标题', max_length=30)
    Jukalail_URL = models.ImageField(u'图片', upload_to='JuKaLaiLe')
    Jukalail_Info = models.CharField(u'内容', max_length=50)

    def __str__(self):
        return self.Jukalail_title

    class Meta:
        verbose_name = "剧咖来了"
        verbose_name_plural = verbose_name
