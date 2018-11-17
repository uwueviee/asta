import discord
import asyncio
import json
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
configJSON = open(os.path.join(__location__, "config.json"), "r")

config = json.load(configJSON)
botToken = config["token"]
prefix = "!"

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!osu'):
        await client.send_message(message.channel, 'https://lemmmy.pw/osusig/sig.php?colour=pink&uname='+message.content.strip('!osu '))

    elif message.content.startswith("!suicide pervention"):
        await client.send_message(message.channel,"Dont do it"+" You are amazing"+" kys")
client.run(botToken)