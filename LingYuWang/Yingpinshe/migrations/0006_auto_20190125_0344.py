# Generated by Django 2.1.4 on 2019-01-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yingpinshe', '0005_auto_20190125_0300'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Yingping_Star_Info_xd',
        ),
        migrations.AlterModelOptions(
            name='yingping_star_info',
            options={'verbose_name': '影评社', 'verbose_name_plural': '影评社'},
        ),
        migrations.RenameField(
            model_name='yingping_star_info',
            old_name='Jukalail_UserName',
            new_name='YingPing_UserName',
        ),
        migrations.AddField(
            model_name='yingping_star_info',
            name='YingPing_Index',
            field=models.IntegerField(default=2, verbose_name='排序'),
        ),
    ]