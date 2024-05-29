from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from items.models import Item
from django.db import models


class Build(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='builds')
    title = models.CharField(max_length=400, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now(), editable=False)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Item, blank=True, through="Important", related_name='builds')

    def __str__(self):
        return f'{self.title} created by {self.author}'

    def get_absolute_url(self):
        return reverse_lazy('build-detail', args=[self.pk])


class Important(models.Model):

    class ItemImportant(models.IntegerChoices):
        NOT_NECESSARY = 0, 'Not necessary'
        PREFERABLY = 1, 'Preferably'
        NEEDED = 2, 'needed'
        NECESSARY = 3, 'Necessary'
        BUILD_BASIS = 4, 'Build basis'

    build = models.ForeignKey(Build, on_delete=models.CASCADE, related_name='items_important')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item')
    item_important = models.PositiveSmallIntegerField(choices=ItemImportant.choices, default=ItemImportant.NEEDED)

    def __str__(self):
        return f'{self.item} | {self.get_item_important_display()}'
