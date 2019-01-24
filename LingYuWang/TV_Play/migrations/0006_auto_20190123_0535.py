# Generated by Django 2.1.4 on 2019-01-23 05:35

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TV_Play', '0005_auto_20190123_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tv_play',
            name='Tv_Info',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='tv_play',
            name='Tv_Url',
            field=models.ImageField(blank=True, upload_to='TV_Play', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='tv_play_xd',
            name='Tv_Info',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='tv_play_xd',
            name='Tv_Url',
            field=models.ImageField(blank=True, upload_to='TV_Play', verbose_name='图片'),
        ),
    ]
