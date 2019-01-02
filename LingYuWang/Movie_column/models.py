from django.db import models

# Create your models here.
class Movie(models.Model):
    img_url = models.ImageField(upload_to='Movie')
    Movie_Title = models.CharField(max_length=30)
    Movie_Info = models.CharField(max_length=150)

