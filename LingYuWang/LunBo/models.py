from django.db import models


# Create your models here.
class LunBo(models.Model):
    LunBo_title = models.CharField(max_length=50)
    LunBo_URL = models.CharField(max_length=50)
