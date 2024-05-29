# Generated by Django 5.0.6 on 2024-05-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0003_alter_build_title'),
        ('items', '0003_alter_addon_image_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='builds', through='builds.Important', to='items.item'),
        ),
    ]