# Generated by Django 2.1.4 on 2019-02-23 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_column', '0010_movie_movie_riqi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Movie_RiQi',
            field=models.DateField(auto_now_add=True, verbose_name='发布日期'),
        ),
    ]
