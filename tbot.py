import os

import discord
from dotenv import load_dotenv
from fastquant import get_pse_data
from fastquant import get_stock_data

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

# @client.event
# async def on_ready():
#     guild = discord.utils.get(client.guilds, name=GUILD)
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name} - (id: {guild.id})'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

# client.run(TOKEN)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Bonjour {member.name}, welcome to the vice den!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = [
        'stock'
    ]

    if message.content.lower().startswith('?phstock'):
        stock = message.content.replace('?phstock ', '')
        response = str(get_pse_data(stock, "2020-11-26", "2020-11-26"))
        await message.channel.send(response)
    elif message.content.lower().startswith('?stock'):
        stock = message.content.replace('?stock ', '')
        response = str(get_stock_data(stock, "2020-11-26", "2020-11-26"))
        await message.channel.send(response)

client.run(TOKEN)