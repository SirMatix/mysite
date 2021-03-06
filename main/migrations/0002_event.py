# Generated by Django 3.2.8 on 2022-04-12 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=128, verbose_name='Event Name')),
                ('event_date', models.DateField(verbose_name='Event Date')),
                ('address', models.CharField(max_length=128, verbose_name='Event Address')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
