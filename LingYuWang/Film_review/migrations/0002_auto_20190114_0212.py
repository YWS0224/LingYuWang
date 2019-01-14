# Generated by Django 2.1.4 on 2019-01-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Film_review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film_review',
            name='f_Info',
            field=models.CharField(max_length=30, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='film_review',
            name='f_Title',
            field=models.CharField(max_length=30, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='film_review',
            name='f_URL',
            field=models.ImageField(upload_to='Film_review', verbose_name='图片'),
        ),
    ]
