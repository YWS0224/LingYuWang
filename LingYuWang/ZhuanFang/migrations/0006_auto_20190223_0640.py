# Generated by Django 2.1.4 on 2019-02-23 06:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ZhuanFang', '0005_auto_20190221_0536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='find_zhuanfang',
            options={'verbose_name': '专访', 'verbose_name_plural': '专访'},
        ),
        migrations.AddField(
            model_name='find_zhuanfang',
            name='ZhuanFang_LaiYu',
            field=models.CharField(default='', max_length=30, verbose_name='来源'),
        ),
        migrations.AddField(
            model_name='find_zhuanfang',
            name='ZhuanFang_RiQi',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='发布日期'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='find_zhuanfang',
            name='ZhuanFang_Type',
            field=models.CharField(default='', max_length=30, verbose_name='分类'),
        ),
    ]