# Generated by Django 2.1 on 2018-09-03 11:04

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0013_auto_20180903_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/pic_folder'), upload_to=''),
        ),
    ]
