from random import randint


def my_insult_bot(discord_client, insults, token):
    @discord_client.event
    async def on_ready():
        print('Logged in as')
        print(discord_client.user.name)
        print(discord_client.user.id)
        print('------')

    @discord_client.event
    async def on_message(message):
        if message.content.startswith('/insult'):
            user = message.content.split(' ')[1]
            await discord_client.send_message(message.channel, '{0} {1}'.format(user, insults[randint(0, len(insults))]))

    discord_client.run(token)
