import discord
import asyncio
import json
import os
import random
from pfaw import Fortnite, Platform, Mode

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
configJSON = open(os.path.join(__location__, "config.json"), "r")

config = json.load(configJSON)
botToken = config["token"]
prefix = "hey asta! "
fortnite = Fortnite(fortnite_token=config["FORTNITE_TOKEN"], launcher_token=config["FORTNITE_LAUNCHER"],
                    password=config["FORTNITE_PASSWORD"], email=config["FORTNITE_EMAIL"])

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.content.startswith(prefix+'test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith(prefix+'sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith(prefix+'osu'):
        newmessage = message.content.split(' ')
        await client.send_message(message.channel, 'https://lemmmy.pw/osusig/sig.php?colour=pink&uname='+newmessage[3])
        print(message.author.name+" just ran !osu with the username being searched "+newmessage[3])
    elif message.content.startswith(prefix+'eightball') or message.content.startswith(prefix+'8ball') or message.content.startswith(prefix+'8-ball') or message.content.startswith(prefix+'eight-ball'):
        num = random.randint(0,6)
        if num == 0:
            await client.send_message(message.channel, 'Certainly!')
        elif num == 1:
            await client.send_message(message.channel, 'Most likely')
        elif num == 2:
            await client.send_message(message.channel, "I'm not sure :/")
        elif num == 3:
            await client.send_message(message.channel, 'Unlikely')
        elif num == 4:
            await client.send_message(message.channel, 'Yes!' )
        elif num == 5:
            await client.send_message(message.channel, 'No!')
        elif num == 6:
            await client.send_message(message.channel, 'Are you crazy?!')
    elif message.content.startswith(prefix+'fortnite'):
        newmessage = message.content.split(' ')
        if newmessage[4] == 'pc':
            stats = fortnite.battle_royale_stats(username=newmessage[3], platform=Platform.pc)
        elif newmessage[4] == 'xbox':
            stats = fortnite.battle_royale_stats(username=newmessage[3], platform=Platform.xb1)
        elif newmessage[4] == 'ps4':
            stats = fortnite.battle_royale_stats(username=newmessage[3], platform=Platform.ps4)
        await client.send_message(message.channel, (f'Solo Wins: {stats.solo.wins}'))
        await client.send_message(message.channel, (f'Duo Wins: {stats.duo.wins}' ))
        await client.send_message(message.channel, (f'Squad Wins: {stats.squad.wins}'))
        await client.send_message(message.channel, (f'Lifetime Wins: {stats.all.wins}'))
        await client.send_message(message.channel, (f'Solo Kills: {stats.solo.kills}'))
        await client.send_message(message.channel, (f'Duo Kills: {stats.duo.kills}'))
        await client.send_message(message.channel, (f'Squads Kills: {stats.squad.kills}'))
        await client.send_message(message.channel, (f'Total Kills: {stats.all.kills}'))
        totalkd = stats.all.kills / (stats.all.matches - stats.all.wins)
        solokd = stats.solo.kills / (stats.solo.matches - stats.solo.wins)
        duokd = stats.duo.kills / (stats.duo.matches - stats.duo.wins)
        squadkd = stats.squad.kills / (stats.squad.matches - stats.squad.wins)
        totalpercent = (stats.all.wins / stats.all.matches)*100
        solopercent = (stats.solo.wins / stats.solo.matches)*100
        duopercent = (stats.duo.wins / stats.duo.matches)*100
        squadpercent = (stats.squad.wins / stats.squad.matches)*100
        await client.send_message(message.channel, (f'Solo matches: {stats.solo.matches}'))
        await client.send_message(message.channel, (f'Duo matches: {stats.duo.matches}'))
        await client.send_message(message.channel, (f'Squads matches: {stats.squad.matches}'))
        await client.send_message(message.channel, (f'Total matches: {stats.all.matches}'))
        await client.send_message(message.channel, (f'Solo KD: {round(solokd,2)}'))
        await client.send_message(message.channel, (f'Duo KD: {round(duokd,2)}'))
        await client.send_message(message.channel, (f'Squads KD: {round(squadkd,2)}'))
        await client.send_message(message.channel, (f'Total KD: {round(totalkd,2)}'))
        await client.send_message(message.channel, (f'Solo win percentage: {round(solopercent,2)}'))
        await client.send_message(message.channel, (f'Duo win percentage: {round(duopercent,2)}'))
        await client.send_message(message.channel, (f'Squads win percentage: {round(squadpercent,2)}'))
        await client.send_message(message.channel, (f'Total win percentage: {round(totalpercent,2)}'))
    elif message.content.startswith(prefix + "death"):
        #await client.send_message(message.channel, "This program will kill someone in your discord sever randomly, would you like to proceed? (type 'YES' for yes, or 'NO' for no): ")
        #if message.content.contains("yes"):
        membersArray = list(message.server.members)
        print(membersArray)
        killed = random.randint(0,len(membersArray)-1)
        print (membersArray[killed])
        print (message.server.get_member(membersArray[killed]))
        await client.send_message(message.channel, message.server.get_member(membersArray[killed]).nick + " was killed by the server") 

client.run(botToken)