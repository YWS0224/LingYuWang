# Generated by Django 2.1.4 on 2019-01-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Star_Photos', '0007_star_photos_jukalail_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='star_photos',
            old_name='Jukalail_UserName',
            new_name='Star_UserName',
        ),
        migrations.AddField(
            model_name='star_photos',
            name='Star_Index',
            field=models.IntegerField(default=2, verbose_name='排序'),
        ),
    ]
