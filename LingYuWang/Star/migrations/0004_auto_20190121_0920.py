# Generated by Django 2.1.4 on 2019-01-21 09:20

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Star', '0003_auto_20190116_0526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Find_Star_Info_xd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Star_Title', models.CharField(max_length=30, verbose_name='标题')),
                ('Star_Url', models.ImageField(upload_to='Star', verbose_name='图片')),
                ('Star_Info', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
            ],
            options={
                'verbose_name': '明星小',
                'verbose_name_plural': '明星小',
            },
        ),
        migrations.AlterModelOptions(
            name='find_star_info',
            options={'verbose_name': '明星大', 'verbose_name_plural': '明星大'},
        ),
    ]
