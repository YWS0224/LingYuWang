# Generated by Django 2.1.4 on 2019-01-23 05:29

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Star_Photos', '0003_auto_20190116_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star_photos',
            name='Star_Info',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
    ]