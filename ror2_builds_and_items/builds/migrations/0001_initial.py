# Generated by Django 5.0.6 on 2024-05-25 09:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, unique_for_date=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='builds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Important',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_important', models.PositiveSmallIntegerField(choices=[(0, 'Not necessary'), (1, 'Preferably'), (2, 'needed'), (3, 'Necessary'), (4, 'Build basis')], default=2)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='build', to='builds.build')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='items.item')),
            ],
        ),
        migrations.AddField(
            model_name='build',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='builds', through='builds.Important', to='items.item'),
        ),
    ]
