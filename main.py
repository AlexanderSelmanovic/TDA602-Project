import discord
from dotenv import load_dotenv

import os
import json
import requests
from discord.ext import commands
from datetime import datetime, timezone

utc_dt = datetime.now(timezone.utc) # UTC time
dt = utc_dt.astimezone() # local time


load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()
client.TOKEN = TOKEN

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        #print(client.user)
        return

    if message.content.startswith('$quote'):
        response = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
        json_data = json.loads(response.text)
        await message.channel.send(str((json_data[0])["quote"]) + '\n - ' + str((json_data[0])["character"]))
        await message.channel.send((json_data[0])["image"])
    else:
        print("User ID: " + str(client.user.id))
        print("Username: " + str(message.author))
        # print(message)
        print("Guild : " + str(message.guild))
        print("Channel: " + str(message.channel.name))
        print("Message: " + str(message.content))
        print("Timestamp: " + str(datetime.now(timezone.utc)))
        print("\n")

client.run(TOKEN)
