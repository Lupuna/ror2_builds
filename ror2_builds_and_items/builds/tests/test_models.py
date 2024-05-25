from tests.test_base import SettingsCase


class TestBuildAndImportantModels(SettingsCase):

    def test_str_method_build(self):
        correct_meaning = f'{self.build.title} created by {self.build.author}'
        print(self.build)
        self.assertEqual(correct_meaning, str(self.build))
