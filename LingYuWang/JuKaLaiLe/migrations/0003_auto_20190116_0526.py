# Generated by Django 2.1.4 on 2019-01-16 05:26

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JuKaLaiLe', '0002_auto_20190114_0212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jukalai_l',
            options={'verbose_name': '剧咖来了', 'verbose_name_plural': '剧咖来了'},
        ),
        migrations.AlterField(
            model_name='jukalai_l',
            name='Jukalail_Info',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
    ]