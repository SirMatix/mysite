# Generated by Django 3.2.8 on 2022-04-12 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 13, 0, 26, 20, 214133), verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 13, 0, 26, 20, 212805), verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(blank=True, max_length=128, verbose_name='Event Address'),
        ),
    ]