import json
from random import randint

import discord

from bot.wot import get_user_id_by_name, get_user_all_stats_by_id

CHANNEL_BLACKLIST = ["schreibstube", "gif-kueche"]


def is_insult(message):
    return message.content.startswith('/insult') and str(message.channel) not in CHANNEL_BLACKLIST


def is_wot(message):
    return message.content.startswith('/wot') and str(message.channel) not in CHANNEL_BLACKLIST


def message_to_str(message: discord.message.Message):
    str_message = {
        'edited_timestamp': message.edited_timestamp,
        'timestamp': message.timestamp,
        'tts': message.tts,
        'content': message.content,
        'channel': message.channel,
        'mention_everyone': message.mention_everyone,
        'embeds': message.embeds,
        'id': message.id,
        'mentions': [member.name for member in message.mentions],
        'mentions.id': [member.id for member in message.mentions],
        'author': message.author.name,
        'author.id': message.author.id,
        'channel_mentions': message.channel_mentions,
        'server': message.server,
        'attachments': message.attachments,
        'nonce': message.nonce,
        'pinned': message.pinned,
        'role_mentions': message.role_mentions,
        'type': message.type,
        'call': message.call,
        'reactions': message.reactions
    }
    return str_message


def my_insult_bot(discord_client, insults, token):
    def send_wot_message(channel, message):
        acc_id = get_user_id_by_name(message.split(' ')[1])
        out = get_user_all_stats_by_id(acc_id)
        return send_message(channel, str(out))

    def send_message(channel, message):
        return discord_client.send_message(channel, message)

    def send_insult(channel, user):
        return send_message(channel, '{0} {1}'.format(user, insults[randint(0, len(insults))]))

    @discord_client.event
    async def on_ready():
        print('Logged in as')
        print(discord_client.user.name)
        print(discord_client.user.id)
        print('------')

    @discord_client.event
    async def on_message(message):
        print(message_to_str(message))
        if discord_client.user.name in message.content:
            await send_message(message.channel,
                               "Hello @{0}! How can I help you?".format(str(message.author).split('#')[0]))
        if is_insult(message):
            user = message.content.split(' ')[1]
            await send_insult(message.channel, user)
        if is_wot(message):
            await send_wot_message(message.channel, message.content)

    discord_client.run(token)
