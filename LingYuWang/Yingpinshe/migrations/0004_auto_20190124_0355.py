# Generated by Django 2.1.4 on 2019-01-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yingpinshe', '0003_auto_20190123_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='yingping_star_info',
            name='Yingping_Title_Keyword',
            field=models.CharField(default='', max_length=30, verbose_name='关键词'),
        ),
        migrations.AddField(
            model_name='yingping_star_info',
            name='Yingping_Title_xd',
            field=models.CharField(default='', max_length=30, verbose_name='小标题'),
        ),
        migrations.AddField(
            model_name='yingping_star_info_xd',
            name='Yingping_Title_Keyword',
            field=models.CharField(default='', max_length=30, verbose_name='关键词'),
        ),
        migrations.AddField(
            model_name='yingping_star_info_xd',
            name='Yingping_Title_xd',
            field=models.CharField(default='', max_length=30, verbose_name='小标题'),
        ),
    ]