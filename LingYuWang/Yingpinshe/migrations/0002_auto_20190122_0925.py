# Generated by Django 2.1.4 on 2019-01-22 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yingpinshe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yingping_star_info',
            name='Yingping_Url',
            field=models.ImageField(upload_to='Yingping', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='yingping_star_info_xd',
            name='Yingping_Url',
            field=models.ImageField(upload_to='Yingping', verbose_name='图片'),
        ),
    ]