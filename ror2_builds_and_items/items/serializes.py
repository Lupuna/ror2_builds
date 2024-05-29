from rest_framework import serializers
from items.models import Item, Addon


class ItemSerializer(serializers.ModelSerializer):

    addon = serializers.StringRelatedField()
    addon_link = serializers.SerializerMethodField()
    rarity_level = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('title', 'description', 'rarity_level', 'image', 'addon', 'addon_link')

    def get_addon_link(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.addon.get_absolute_url())

    def get_rarity_level(self, obj):
        return obj.get_rarity_level_display()


class AddonSerializer(serializers.ModelSerializer):

    items = serializers.StringRelatedField(many=True)
    items_links = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Addon
        fields = ('title', 'description', 'image', 'items', 'items_links')

    def get_items_links(self, obj):
        request = self.context.get('request')
        return [request.build_absolute_uri(item.get_absolute_url()) for item in obj.items.all()]

