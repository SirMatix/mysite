# Generated by Django 3.2.8 on 2022-04-13 00:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220413_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 13, 1, 25, 52, 346476), verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 13, 1, 25, 52, 346476), verbose_name='Start Date'),
        ),
    ]