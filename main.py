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
        #print(str((json_data[0])["quote"]) + ' - ' + str((json_data[0])["character"] + '\n' + str((json_data[0])["image"])))
        await message.channel.send(str((json_data[0])["quote"]) + '\n - ' + str((json_data[0])["character"]))# + '\n' + (json_data[0])["image"])
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

    # async for guild in client.fetch_guilds(limit=150):
    #     print(guild.name)
    
    # await request_offline_members(guild)
    # for member in guild.members:
    #     print(member)

    # headers = {
    # 'Authorization': 'Bot ODI3MDkyOTk4MjM2MDEyNTQ2.YGWAYQ.E_lszP4vS1aEB9DjTVbf5z2fBAE'   
    # }

    # botid = '827080071822573590'
    # # params = {
    # # 'limit':'50',
    # # 'user_id': '393051363883352066',
    # # 'action_type': '40',
    # # 'authorization': 'Bot ODI3MDkyOTk4MjM2MDEyNTQ2.YGWAYQ.E_lszP4vS1aEB9DjTVbf5z2fBAE'
    # # }

    # # id = message.author.id
    # response = requests.get("https://discord.com/api/v8/users/393051363883352066", headers=headers)#${id}")
    # json_data = json.loads(response.text)
    # print(json_data)

    # response = requests.get("https://discord.com/api/v8/guilds/827080071822573587/members", headers=headers)#${id}")
    # json_data = json.loads(response.text)
    # print(json_data)

    # await ctx.message.server.get_member("id") or message.server.get_member("id")

# @client.event
# async on_react(message):
#     i


client.run(TOKEN)
