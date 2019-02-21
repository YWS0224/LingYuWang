from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class Find_DUJIACEHUA(models.Model):
    CEHUA_title = models.CharField(max_length=20)
