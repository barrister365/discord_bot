import boto.gs.user
import discord
from discord.ext import commands

# client = discord.Client(intents=discord.Intents())
bot = commands.Bot(command_prefix='.', intents=discord.Intents())


@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        await ctx.reply(ctx.content)


bot.run('MTA4Njk2MjkxMDIwMDM0NDY3OA.GA8rfa.-WCuZEcRU-IQcl3dqjb9dHkuwLiAqe3cGCsd-Q')
