# Generated by Django 2.1 on 2018-08-31 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_auto_20180830_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor_info',
            name='category',
            field=models.CharField(choices=[('em', 'Electronics Material'), ('cf', 'Cloths_Food'), ('edum', 'Education Material'), ('ot', 'Other')], default=1, max_length=4),
            preserve_default=False,
        ),
    ]