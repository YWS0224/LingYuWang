# Generated by Django 2.1.4 on 2019-01-23 05:29

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TV_Play', '0004_auto_20190121_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tv_play',
            name='Tv_Info',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='tv_play_xd',
            name='Tv_Info',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
    ]
