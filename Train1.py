import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='.', intents=discord.Intents())


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def remindme(ctx, time: int, message: str):
    await bot.say('Reminder set!')
    await asyncio.sleep(time)
    await bot.say('Reminder: {}'.format(message))


bot.run('MTA4Njk2MjkxMDIwMDM0NDY3OA.GA8rfa.-WCuZEcRU-IQcl3dqjb9dHkuwLiAqe3cGCsd-Q')
