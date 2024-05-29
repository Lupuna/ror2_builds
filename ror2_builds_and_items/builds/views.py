from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializes, models


class BuildView(ModelViewSet):

    serializer_class = serializes.BuildSerializer
    queryset = models.Build.objects.all().select_related('author').prefetch_related('items_important', 'items')
