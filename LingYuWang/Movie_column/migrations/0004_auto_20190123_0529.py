# Generated by Django 2.1.4 on 2019-01-23 05:29

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_column', '0003_auto_20190116_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Movie_Info',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='movie_xiaode',
            name='Movie_Info',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
    ]
