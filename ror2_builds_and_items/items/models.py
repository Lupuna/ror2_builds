from django.db import models


class Addon(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/', default='icon.svg')

    def __str__(self):
        return self.title


class Item(models.Model):

    class RarityLevel(models.IntegerChoices):
        COMMON = 0, 'Common'
        RARE = 1, 'Rare'
        EPIC = 2, 'Epic'
        LEGENDARY = 3, 'Legendary'

    title = models.CharField(max_length=40, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    rarity_level = models.PositiveSmallIntegerField(choices=RarityLevel.choices, default=RarityLevel.COMMON)
    image = models.ImageField(upload_to='images/%Y/%m/', default='icon.svg')
    addon = models.ForeignKey(Addon, on_delete=models.PROTECT, related_name='items')

    def __str__(self):
        return self.title
