# Generated by Django 5.0.6 on 2024-05-29 04:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0004_alter_build_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 4, 30, 4, 594245, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='title',
            field=models.CharField(max_length=400, unique_for_date='publish'),
        ),
    ]