# Generated by Django 5.0.6 on 2024-05-25 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_addon_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addon',
            name='image',
            field=models.ImageField(default='icon.svg', upload_to='images/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='icon.svg', upload_to='images/%Y/%m/'),
        ),
    ]