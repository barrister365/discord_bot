import discord
import asyncio

from discord import message

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    channel = client.get_channel('1073703847178014822') # Replace <channel_id> with the ID of the channel you want to post to
    while True:
        await message.(channel, 'This is an automated message!')
        await asyncio.sleep(40) # Sleep for 40 seconds

client.run('MTA4Njk2MjkxMDIwMDM0NDY3OA.GA8rfa.-WCuZEcRU-IQcl3dqjb9dHkuwLiAqe3cGCsd-Q')