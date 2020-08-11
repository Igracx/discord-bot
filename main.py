import discord
from discord.ext import commands
import commands_define as cdef

# ENTER YOUR TOKEN HERE
TOKEN = "NzQxOTg2NzkyNTUwNjk0OTI0.Xy_jDA.pnLaLK34PXyfaGo9kBCbHgbO26I"
#TOKEN = "NTI4OTY4MDM4NzcxNDU4MDcz.XCjt4A.r-4_MurOpZcIDfxCLhrsXPv5CuY"

client = commands.Bot(command_prefix='!')
client.remove_command('help')

@client.event # event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")

# commands
@client.command(pass_context=True)
async def roll_dice(ctx):
    await ctx.message.delete()
    await cdef.roll_dice(ctx)

@client.command(pass_context=True)
async def help(ctx):
    await ctx.message.delete()
    await cdef.print_help_message(ctx)

@client.command(pass_context=True)
async def pomoc(ctx):
    await ctx.message.delete()
    await cdef.print_pomoc_message(ctx)

@client.command(pass_context=True)
async def join_voice(ctx):
    channel = ctx.message.author.voice.channel
    await ctx.message.delete()
    vc = await channel.connect()

@client.command(pass_context=True)
async def leave_voice(ctx):
    await ctx.voice_client.disconnect()
    await ctx.message.delete()

client.run(TOKEN)