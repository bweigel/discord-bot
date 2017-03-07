from unittest import TestCase

from bot.insults import is_insult
from discord.message import Message
from discord.channel import Channel


class TestIs_insult(TestCase):
    def test_is_insult(self):
        message = Message()
        message.author("eigelb")
        message.channel
        self.assertTrue(is_insult(message))
        self.fail()
