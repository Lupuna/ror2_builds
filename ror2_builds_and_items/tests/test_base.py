from django.contrib.auth.models import User
from items.models import Item, Addon
from builds.models import Build, Important
from django.test import TestCase


class SettingsCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='test_username_1',
            password='test_password_1'
        )

        cls.addon = Addon.objects.create(
            title='test_addon_title_1',
        )

        cls.item = Item.objects.create(
            title='test_item_title_1',
            addon=cls.addon
        )

        cls.build = Build.objects.create(
            author=cls.user,
            title='test_build_title_1'
        )

        cls.build.items.add(cls.item)
