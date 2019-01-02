from django.db import models

# Create your models here.

class film_review(models.Model):
    f_Title = models.CharField(max_length=30)
    f_Info = models.CharField(max_length=30)
    f_URL = models.CharField(max_length=30)
