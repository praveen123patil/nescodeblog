# Generated by Django 2.1 on 2018-08-31 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0005_auto_20180830_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='city',
            field=models.CharField(choices=[('Bgm', 'Belgaum'), ('Bgr', 'Banglore'), ('Hub', 'Hubali'), ('Dhr', 'Dharwad'), ('Pun', 'Pune'), ('Mum', 'Mumbai')], max_length=3),
        ),
        migrations.AlterField(
            model_name='donors',
            name='p_name',
            field=models.CharField(max_length=20),
        ),
    ]
