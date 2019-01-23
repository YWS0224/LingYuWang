# Generated by Django 2.1.4 on 2019-01-22 09:01

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yingping_Star_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yingping_Title', models.CharField(max_length=30, verbose_name='标题')),
                ('Yingping_Url', models.ImageField(upload_to='Star', verbose_name='图片')),
                ('Yingping_Info', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
            ],
            options={
                'verbose_name': '影评社大',
                'verbose_name_plural': '影评社大',
            },
        ),
        migrations.CreateModel(
            name='Yingping_Star_Info_xd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yingping_Title', models.CharField(max_length=30, verbose_name='标题')),
                ('Yingping_Url', models.ImageField(upload_to='Star', verbose_name='图片')),
                ('Yingping_Info', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
            ],
            options={
                'verbose_name': '影评社小',
                'verbose_name_plural': '影评社小',
            },
        ),
    ]
