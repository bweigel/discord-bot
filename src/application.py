import discord

from bot.insults import my_insult_bot
from util.insults import read_insults
from util.kms import kms_decrypt_token

ENCRYPTED_BOT_TOKEN = 'AQECAHhGzpV8mQljdA8TKn6ES9Tut5So2p1aU1owbT61BvTSSgAAAJ0wgZoGCSqGSIb3DQEHBqCBjDCBiQIBADCBgwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzyk8NnIh7IjL9rvaoCARCAVmWPRwmvkXDpq/ATmZkzOmJQruvz4zSyzJkkJUnd8BqWvGGK2cursFqcPvBzMYLejsAaNkB0lCnHOcoP7sVXVuSB2q0uq+ula+3nfTgRGi1QJfISTSeE'


if __name__ == "__main__":
    my_insult_bot(discord_client=discord.Client(),
                  insults=read_insults(),
                  token=kms_decrypt_token(ENCRYPTED_BOT_TOKEN))

