# Generated by Django 2.1 on 2018-08-31 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor_info',
            name='email',
        ),
        migrations.AddField(
            model_name='donor_info',
            name='price',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]