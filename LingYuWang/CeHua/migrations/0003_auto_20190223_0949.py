# Generated by Django 2.1.4 on 2019-02-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CeHua', '0002_auto_20190223_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cehua_photos',
            name='CeHua_Url',
        ),
        migrations.AddField(
            model_name='cehua_photos',
            name='CeHuaTitle_xd',
            field=models.CharField(default='', max_length=30, verbose_name='小标题'),
        ),
        migrations.AddField(
            model_name='cehua_photos',
            name='CeHua_Type',
            field=models.CharField(default='', max_length=30, verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='cehua_photos',
            name='CeHua_url',
            field=models.ImageField(blank=True, upload_to='Movie', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='cehua_photos',
            name='CeHua_Title_Keyword',
            field=models.CharField(default='', max_length=30, verbose_name='关键字'),
        ),
    ]