import discord
from discord.ext import commands
TOKEN=''

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
pp = commands.Bot(command_prefix='.', intents = intents)

@pp.event
async def on_ready():
    print('Ready and at your service')
@pp.event
async def on_member_remove(member):
    print(f'{member}  has left the server')
@pp.event
async def on_member_join(member):
    print(f'{member}  has joined the server')

@pp.command()
async def hi(ctx):
    await ctx.send("Hello!")
@pp.command()
async def ping(ctx):
    await ctx.send(f'My latency is {round(pp.latency * 1000)}ms')
#---
@pp.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'{amount} messages cleared')
@pp.command()
@commands.has_permissions(manage_messages=True)
async def silent_clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)
@pp.command()
@commands.has_permissions(manage_messages=True)
async def purge_channel(ctx, amount=200):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send('This channel has been purged and 200 messages deleted.')
#---
def if_the_admin(ctx):
    return ctx.author.id == <><><><>SERVER ADMIN ID HERE<><><><>
@pp.command()
@commands.check(if_the_admin)
async def kick(ctx, member : discord.Member, *, reason=None, user=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} was kicked because {reason}')
@pp.command()
@commands.check(if_the_admin)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned: {member.mention}')
@pp.command()
@commands.check(if_the_admin)
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
#---
pp.run(TOKEN)
