# Generated by Django 2.1.4 on 2019-01-25 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Welfare', '0006_auto_20190124_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='find_welfare_info',
            name='Jukalail_UserName',
            field=models.CharField(default='', max_length=30, verbose_name='编辑名称'),
        ),
    ]
