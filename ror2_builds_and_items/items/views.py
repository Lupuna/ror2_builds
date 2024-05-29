from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from items.models import Item, Addon
from items.serializes import AddonSerializer, ItemSerializer


class AddonView(ModelViewSet):
    queryset = Addon.objects.all().prefetch_related('items')
    serializer_class = AddonSerializer


class ItemView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

