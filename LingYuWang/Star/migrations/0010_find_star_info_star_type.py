# Generated by Django 2.1.4 on 2019-02-23 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Star', '0009_auto_20190125_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='find_star_info',
            name='Star_Type',
            field=models.CharField(default='', max_length=30, verbose_name='分类'),
        ),
    ]
