import random
import discord
from discord.ext import commands
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
pp = commands.Bot(command_prefix='.', intents = intents)

@pp.event
async def on_ready():
    print('Ready and at your service')
@pp.event
async def on_member_join(member):
    print(f'{member}  has joined the server')
@pp.event
async def on_member_remove(member):
    print(f'{member}  has left the server')


@pp.command()
async def hi(ctx):
    await ctx.send("Hello!")
@pp.command()
async def ping(ctx):
    await ctx.send(f'{round(pp.latency * 1000)}ms')
@pp.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'{amount} messages cleared')

    
@pp.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
@pp.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned: {member.mention}')
"""After an hour I did have to copy this unban part"""
@pp.command()
async def unban(ctx, *, user=None):
    try:
        user = await commands.converter.UserConverter().convert(ctx, user)
    except:
        await ctx.send("Error: user could not be found!")
        return
    try:
        bans = tuple(ban_entry.user for ban_entry in await ctx.guild.bans())
        if user in bans:
            await ctx.guild.unban(user, reason="Responsible moderator: "+ str(ctx.author))
        else:
            await ctx.send("User not banned")
            return
    except discord.Forbidden:
        await ctx.send("I don't have permission to unban")
        return
    except:
        await ctx.send("Unbanning failed")
        return
    await ctx.send(f"Unbanned {user.mention}!")

pp.run('token')
