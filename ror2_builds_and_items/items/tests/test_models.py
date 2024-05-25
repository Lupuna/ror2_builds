from tests.test_base import SettingsCase


class TestItemAndAddonModels(SettingsCase):

    def test_str_method_addon(self):
        correct_meaning = self.addon.title
        self.assertEqual(correct_meaning, str(self.addon))

    def test_str_method_item(self):
        correct_meaning = self.item.title
        self.assertEqual(correct_meaning, str(self.item))
