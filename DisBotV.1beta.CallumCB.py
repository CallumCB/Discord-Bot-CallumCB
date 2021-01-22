import random
import discord
from discord.ext import commands

#intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
#client = commands.Bot(command_prefix = '*', intents = intents)

pp = commands.Bot(command_prefix='?')

@pp.event
async def on_ready():
    print('Ready and at your service')

@pp.command()
async def hi(ctx):
    await ctx.send("Hello!")

@pp.command()
async def ping(ctx):
    await ctx.send('Pong!')

@pp.event
async def on_member_join(member):
    print('f {member} has joined a server')

@pp.event
async def on_member_remove(member):
    print('f {member}has left a server')



pp.run('TOKEN')
