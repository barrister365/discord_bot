import asyncio
import random
import discord
from discord.ext import commands
import time


client = discord.Client(intents=discord.Intents())
#bot = commands.Bot(command_prefix='!', intents=discord.Intents())


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')


client.run('_')
