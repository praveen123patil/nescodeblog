# Generated by Django 2.1 on 2018-09-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0012_auto_20180903_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='img',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='media/pic_folder/'),
        ),
    ]
