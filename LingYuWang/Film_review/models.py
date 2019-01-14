from django.db import models

# Create your models here.

class film_review(models.Model):
    f_Title = models.CharField(u'标题', max_length=30)
    f_Info = models.CharField(u'内容', max_length=30)
    f_URL = models.ImageField(u'图片', upload_to='Film_review')

    def __str__(self):
        return self.f_Title

    class Meta:
        verbose_name = "影评"
        verbose_name_plural = verbose_name
