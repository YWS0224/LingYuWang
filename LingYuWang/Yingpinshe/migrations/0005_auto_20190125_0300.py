# Generated by Django 2.1.4 on 2019-01-25 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yingpinshe', '0004_auto_20190124_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='yingping_star_info',
            name='Jukalail_UserName',
            field=models.CharField(default='', max_length=30, verbose_name='编辑名称'),
        ),
        migrations.AddField(
            model_name='yingping_star_info_xd',
            name='Jukalail_UserName',
            field=models.CharField(default='', max_length=30, verbose_name='编辑名称'),
        ),
    ]
