from base64 import b64decode
from random import randint

import discord
import boto3

ENCRYPTED_BOT_TOKEN = 'AQECAHhGzpV8mQljdA8TKn6ES9Tut5So2p1aU1owbT61BvTSSgAAAJ0wgZoGCSqGSIb3DQEHBqCBjDCBiQIBADCBgwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzyk8NnIh7IjL9rvaoCARCAVmWPRwmvkXDpq/ATmZkzOmJQruvz4zSyzJkkJUnd8BqWvGGK2cursFqcPvBzMYLejsAaNkB0lCnHOcoP7sVXVuSB2q0uq+ula+3nfTgRGi1QJfISTSeE'


def kms_decrypt_token(token):
    kms = boto3.client('kms')
    return kms.decrypt(CiphertextBlob=b64decode(token))['Plaintext'].decode('utf-8')


def read_insults():
    with open("insults.txt", 'r') as fi:
        insults = fi.read()
    return insults.split("\n")


if __name__ == "__main__":
    client = discord.Client()
    insults = read_insults()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        if message.content.startswith('/insult'):
            user = message.content.split(' ')[1]
            await client.send_message(message.channel, '{0} {1}'.format(user, insults[randint(0,len(insults))]))

    client.run(kms_decrypt_token(ENCRYPTED_BOT_TOKEN))
