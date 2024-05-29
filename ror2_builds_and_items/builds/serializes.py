from rest_framework import serializers
from builds.models import Build, Important


class BuildSerializer(serializers.ModelSerializer):
    updated = serializers.DateTimeField(source='build.updated', read_only=True)
    created = serializers.DateTimeField(source='build.created', read_only=True)
    author = serializers.CharField(source='author.username')
    items_important = serializers.SerializerMethodField()

    class Meta:
        model = Build
        fields = ('author', 'title', 'description', 'updated', 'created', 'items_important')

    def get_items_important(self, obj):
        items = map(str, obj.items.all())
        return dict(zip(items, [item.get_item_important_display() for item in obj.items_important.all()]))
