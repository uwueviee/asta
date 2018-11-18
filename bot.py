import discord
import asyncio
import json
import os
import random
from pfaw import Fortnite, Platform, Mode
from weather import Weather, Unit

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
        if newmessage.index('pc') > -1:
            name = ""
            for x in range(3,newmessage.index('pc')):
                if x != 3:
                    name = name + " " + newmessage[x]
                else:
                    name = name + newmessage[x]
            stats = fortnite.battle_royale_stats(username=name, platform=Platform.pc)
        elif newmessage.index('xbox') > -1:
            name = ""
            for x in range(3,newmessage.index('xbox')):
                if x != 3:
                    name = name + " " + newmessage[x]
                else:
                    name = name + newmessage[x]
            stats = fortnite.battle_royale_stats(username=name, platform=Platform.xb1)
        elif newmessage.index('ps4') > -1:
            name = ""
            for x in range(3,newmessage.index('ps4')):
                if x != 3:
                    name = name + " " + newmessage[x]
                else:
                    name = name + newmessage[x]
            stats = fortnite.battle_royale_stats(username=name, platform=Platform.ps4)
        
        if stats.all.kills == 0 or stats.all.matches == 0:
            totalkd = 0
        else:
            totalkd = stats.all.kills / (stats.all.matches - stats.all.wins)
        
        if stats.solo.kills == 0 or stats.solo.matches == 0:
            solokd = 0
        else:
            solokd = stats.solo.kills / (stats.solo.matches - stats.solo.wins)
        
        if stats.duo.kills == 0 or stats.duo.matches == 0:
            duokd = 0
        else:
            duokd = stats.duo.kills / (stats.duo.matches - stats.duo.wins)
        
        if stats.squad.kills == 0 or stats.squad.matches == 0:
            squadkd = 0
        else:
            squadkd = stats.squad.kills / (stats.squad.matches - stats.squad.wins)
        
        if stats.all.wins == 0 or stats.all.matches == 0:
            totalpercent = 0
        else:
            totalpercent = (stats.all.wins / stats.all.matches)*100
        
        if stats.solo.wins == 0 or stats.solo.matches == 0:
            solopercent = 0
        else:
            solopercent = (stats.solo.wins / stats.solo.matches)*100
        
        if stats.duo.wins == 0 or stats.duo.matches == 0:
            duopercent = 0
        else:
            duopercent = (stats.duo.wins / stats.duo.matches)*100
        
        if stats.squad.wins == 0 or stats.squad.matches == 0:
            squadpercent = 0
        else:
            squadpercent = (stats.squad.wins / stats.squad.matches)*100
        embed = discord.Embed(title=name+"'s Fortnite Stats", colour=discord.Colour(0x56faf6), url="", description="")
        embed.set_thumbnail(url="")
        embed.set_author(name="ASTA", url="https://discordapp.com", icon_url="")
        embed.set_footer(text="ASTA Fortnite Stats", icon_url="")
        embed.add_field(name="Solo Wins:", value=stats.solo.wins)
        embed.add_field(name="Duo Wins:", value=stats.duo.wins)
        embed.add_field(name="Squad Wins:", value=stats.squad.wins)
        embed.add_field(name="Solo Kills:", value=stats.solo.kills)
        embed.add_field(name="Duo Kills:", value=stats.duo.kills)
        embed.add_field(name="Squad Kills:", value=stats.squad.kills)
        embed.add_field(name="Solo Matches:", value=stats.solo.matches)
        embed.add_field(name="Duo Matches:", value=stats.duo.matches)
        embed.add_field(name="Squad KDR:", value=stats.squad.matches)
        embed.add_field(name="Solo KDR:", value=round(solokd,2))
        embed.add_field(name="Duo KDR:", value=round(duokd,2))
        embed.add_field(name="Squad KDR:", value=round(squadkd,2))
        embed.add_field(name="Solo Win Percentage:", value=round(solopercent,2))
        embed.add_field(name="Duo Win Percentage:", value=round(duopercent,2))
        embed.add_field(name="Squad Win Percentage:", value=round(squadpercent,2))
        embed.add_field(name="Liftime Wins:", value=stats.all.wins)
        embed.add_field(name="Lifetime Kills:", value=stats.all.kills)
        embed.add_field(name="Lifetime Matches:", value=stats.all.matches)
        embed.add_field(name="Lifetime KDR:", value=round(totalkd,2))
        embed.add_field(name="Lifetime Win Percentage:", value=round(totalpercent,2))
        await client.send_message(message.channel, embed=embed)
    elif message.content.startswith(prefix+'weather'):
        messagelist = message.content.split(' ')
        weather = Weather(unit=Unit.CELSIUS)
        location = weather.lookup_by_location(messagelist[2])
        conditions = location.condition
        print (conditions)
        await client.send_message(message.channel, conditions.text)
client.run(botToken)