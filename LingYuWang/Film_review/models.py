from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class film_review(models.Model):
    f_Title = models.CharField(u'标题', max_length=30)
    f_URL = models.ImageField(u'图片', upload_to='Film_review')
    f_Info = UEditorField(verbose_name=u'内容', width=800, height=600, imagePath="courses/ueditor/",
                             filePath="courses/ueditor/", default='')

    def __str__(self):
        return self.f_Title

    class Meta:
        verbose_name = "影评"
        verbose_name_plural = verbose_name
