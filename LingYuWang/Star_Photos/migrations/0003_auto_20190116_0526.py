# Generated by Django 2.1.4 on 2019-01-16 05:26

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Star_Photos', '0002_auto_20190114_0212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='star_photos',
            options={'verbose_name': '明星美图', 'verbose_name_plural': '明星美图'},
        ),
        migrations.AlterField(
            model_name='star_photos',
            name='Star_Info',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
    ]