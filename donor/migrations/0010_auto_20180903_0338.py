# Generated by Django 2.1 on 2018-09-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0009_donors_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='img',
            field=models.ImageField(upload_to='media/pic_folder/'),
        ),
    ]