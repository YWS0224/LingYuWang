# Generated by Django 2.1.4 on 2019-01-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Star', '0006_auto_20190123_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='find_star_info',
            name='Star_Title_Keyword',
            field=models.CharField(default='', max_length=30, verbose_name='关键词'),
        ),
        migrations.AddField(
            model_name='find_star_info',
            name='Star_Title_xd',
            field=models.CharField(default='', max_length=30, verbose_name='小标题'),
        ),
        migrations.AddField(
            model_name='find_star_info_xd',
            name='Star_Title_Keyword',
            field=models.CharField(default='', max_length=30, verbose_name='关键词'),
        ),
        migrations.AddField(
            model_name='find_star_info_xd',
            name='Star_Title_xd',
            field=models.CharField(default='', max_length=30, verbose_name='小标题'),
        ),
    ]
