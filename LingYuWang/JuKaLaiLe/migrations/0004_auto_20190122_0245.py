# Generated by Django 2.1.4 on 2019-01-22 02:45

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JuKaLaiLe', '0003_auto_20190116_0526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jukalai_L_Xd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jukalail_title', models.CharField(max_length=30, verbose_name='标题')),
                ('Jukalail_URL', models.ImageField(upload_to='JuKaLaiLe', verbose_name='图片')),
                ('Jukalail_Info', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
            ],
            options={
                'verbose_name': '剧咖来了小',
                'verbose_name_plural': '剧咖来了小',
            },
        ),
        migrations.AlterModelOptions(
            name='jukalai_l',
            options={'verbose_name': '剧咖来了大', 'verbose_name_plural': '剧咖来了大'},
        ),
    ]
