# Generated by Django 2.1.4 on 2018-12-31 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=30)),
                ('Movie_Title', models.CharField(max_length=30)),
                ('Movie_Info', models.CharField(max_length=150)),
            ],
        ),
    ]
