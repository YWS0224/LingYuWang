# Generated by Django 2.1.4 on 2019-01-16 05:26

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Welfare', '0002_auto_20190114_0212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='find_welfare_info',
            options={'verbose_name': '福利社', 'verbose_name_plural': '福利社'},
        ),
        migrations.AlterField(
            model_name='find_welfare_info',
            name='Walfare_Info',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
    ]
