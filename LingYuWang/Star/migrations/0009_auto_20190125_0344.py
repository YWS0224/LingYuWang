# Generated by Django 2.1.4 on 2019-01-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Star', '0008_auto_20190125_0300'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Find_Star_Info_xd',
        ),
        migrations.AlterModelOptions(
            name='find_star_info',
            options={'verbose_name': '明星', 'verbose_name_plural': '明星'},
        ),
        migrations.RenameField(
            model_name='find_star_info',
            old_name='Jukalail_UserName',
            new_name='Star_UserName',
        ),
        migrations.AddField(
            model_name='find_star_info',
            name='Star_Index',
            field=models.IntegerField(default=2, verbose_name='排序'),
        ),
    ]
