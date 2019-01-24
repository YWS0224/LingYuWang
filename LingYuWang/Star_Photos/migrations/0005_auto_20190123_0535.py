# Generated by Django 2.1.4 on 2019-01-23 05:35

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Star_Photos', '0004_auto_20190123_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star_photos',
            name='Star_Info',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='star_photos',
            name='Star_Url',
            field=models.ImageField(blank=True, upload_to='Star_Photos', verbose_name='图片'),
        ),
    ]