# Generated by Django 2.1.4 on 2019-01-07 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jukalai_L',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jukalail_title', models.CharField(max_length=30)),
                ('Jukalail_URL', models.ImageField(upload_to='img')),
                ('Jukalail_Info', models.CharField(max_length=50)),
            ],
        ),
    ]