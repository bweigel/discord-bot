from unittest import TestCase

from bot.wot import get_user_id_by_name


class TestGet_user_id_by_name(TestCase):
    def test_get_user_id_by_name(self):
        self.assertEqual(get_user_id_by_name("Duselmanus"), 504318824)
