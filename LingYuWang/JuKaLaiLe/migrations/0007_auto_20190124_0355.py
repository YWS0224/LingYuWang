# Generated by Django 2.1.4 on 2019-01-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JuKaLaiLe', '0006_auto_20190123_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='jukalai_l',
            name='Jukalail_title_Keyword',
            field=models.CharField(default='', max_length=30, verbose_name='关键词'),
        ),
        migrations.AddField(
            model_name='jukalai_l',
            name='Jukalail_title_xd',
            field=models.CharField(default='', max_length=30, verbose_name='小标题'),
        ),
        migrations.AddField(
            model_name='jukalai_l_xd',
            name='Jukalail_title_Keyword',
            field=models.CharField(default='', max_length=30, verbose_name='关键词'),
        ),
        migrations.AddField(
            model_name='jukalai_l_xd',
            name='Jukalail_title_xd',
            field=models.CharField(default='', max_length=30, verbose_name='小标题'),
        ),
    ]
