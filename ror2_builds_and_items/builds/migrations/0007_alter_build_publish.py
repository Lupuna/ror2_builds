# Generated by Django 5.0.6 on 2024-05-29 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0006_alter_build_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 9, 5, 14, 101785, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
