# Generated by Django 2.1.4 on 2019-02-23 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_column', '0008_auto_20190125_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Movie_LaiYuan',
            field=models.CharField(default='', max_length=30, verbose_name='来源'),
        ),
        migrations.AddField(
            model_name='movie',
            name='Movie_Type',
            field=models.CharField(default='', max_length=30, verbose_name='分类'),
        ),
    ]