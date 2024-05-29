# Generated by Django 5.0.6 on 2024-05-29 09:36

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0007_alter_build_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 9, 36, 40, 118869, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='important',
            name='build',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_important', to='builds.build'),
        ),
    ]