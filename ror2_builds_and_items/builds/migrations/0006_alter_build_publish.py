# Generated by Django 5.0.6 on 2024-05-29 04:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0005_build_publish_alter_build_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 4, 32, 36, 150693, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]