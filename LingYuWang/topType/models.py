from django.db import models

# Create your models here.
class Top_Type(models.Model):
    TopType = models.CharField(max_length=30)
