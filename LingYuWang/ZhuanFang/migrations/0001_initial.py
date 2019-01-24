# Generated by Django 2.1.4 on 2019-01-23 06:00

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Find_ZhuanFang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ZhuanFang_Title', models.CharField(max_length=30, verbose_name='标题')),
                ('ZhuanFang_Url', models.ImageField(blank=True, upload_to='ZhuanFang', verbose_name='图片')),
                ('ZhuanFang_Info', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('ZhuanFang_sTitle', models.CharField(max_length=50, verbose_name='小标题')),
            ],
            options={
                'verbose_name': '专访大',
                'verbose_name_plural': '专访大',
            },
        ),
        migrations.CreateModel(
            name='Find_ZhuanFang_XD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ZhuanFang_Title', models.CharField(max_length=30, verbose_name='标题')),
                ('ZhuanFang_Url', models.ImageField(blank=True, upload_to='ZhuanFang', verbose_name='图片')),
                ('ZhuanFang_Info', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('ZhuanFang_sTitle', models.CharField(max_length=50, verbose_name='小标题')),
            ],
            options={
                'verbose_name': '专访小',
                'verbose_name_plural': '专访小',
            },
        ),
    ]
