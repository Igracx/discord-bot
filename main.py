from discord.ext import commands
import commands_define as cdef
import youtube_dl
import asyncio
import discord
import shutil
import os

# ENTER YOUR TOKEN HERE
TOKEN = "NzQxOTg2NzkyNTUwNjk0OTI0.Xy_jDA.8bzKPdEhnEmxw9XRHN0vReSyjUU"

client = commands.Bot(command_prefix="!")
client.remove_command('help')

# setup for music commands

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

# '%(extractor)s-%(id)s-%(title)s.%(ext)s'

download_dir = "music_tmp"
if "music_tmp" in os.listdir():
    shutil.rmtree(download_dir)
os.mkdir(download_dir)

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(download_dir, "%(title)s.%(ext)s"),
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        print(f"Downloading video: \"{data['title']}\"\turl={data['webpage_url']}")
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


# music commands

music_queue = []

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        await ctx.message.delete()
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await ctx.message.delete()
        await channel.connect()


    @commands.command()
    async def addq(self, ctx, *args):
        """Downloads audio file from the url, and adds it to the que, anythin youtube-dl supports"""

        print(f"{ctx.message.author}: {ctx.message.content}")
        await ctx.message.delete()
        for url in args:
            source = await YTDLSource.from_url(url, loop=self.client.loop)
            music_queue.append(source)


    @commands.command()
    async def pque(self, ctx):
        """Start playing songs in queue, starting from the first added song"""

        print(f"{ctx.message.author}: {ctx.message.content}")
        await ctx.message.delete()
        channel = ctx.channel
        voice = ctx.voice_client

        if len(music_queue) == 0:
            return

        def play_next(ctx):
            if len(music_queue) == 0:
                return

            source = music_queue.pop(0)
            voice.play(source, after=lambda e: play_next(ctx))
            voice.is_playing() 

        if channel and not voice.is_playing():
            source = music_queue.pop(0)
            voice.play(source, after=lambda e: play_next(ctx))
            voice.is_playing()


    @commands.command()
    async def stupid(self, ctx, at=None):

        filename = "stupid_audio.m4a"
        if at is not None:
            await ctx.send(f"{at} is stupid!")

        print(f"{ctx.message.author}: {ctx.message.content}")
        await ctx.message.delete()
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(filename))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)


    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        print(f"{ctx.message.author}: {ctx.message.content}")
        await ctx.message.delete()
        await ctx.voice_client.disconnect()

    @pque.before_invoke
    @stupid.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


# non music related commands

@client.command(pass_context=True)
async def roll_dice(ctx):
    """Rolls dice, returns random number between 1 and 6"""

    print(f"{ctx.message.author}: {ctx.message.content}")
    await ctx.message.delete()
    await cdef.roll_dice(ctx)

@client.command(pass_context=True)
async def roll_dice_deprecated(ctx):
    """Same as roll_dice, just basic text, no formating
        deprecated version """

    print(f"{ctx.message.author}: {ctx.message.content}")
    await ctx.message.delete()
    await cdef.roll_dice_deprecated(ctx)

@client.command(pass_context=True)
async def help(ctx):
    """prints command and what they do"""

    print(f"{ctx.message.author}: {ctx.message.content}")
    await ctx.message.delete()
    await cdef.print_help_message(ctx)

@client.command(pass_context=True)
async def pomoc(ctx):
    """prints help in Serbian language"""

    print(f"{ctx.message.author}: {ctx.message.content}")
    await ctx.message.delete()
    await cdef.print_pomoc_message(ctx)

@client.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('------')

client.add_cog(Music(client))
client.run(TOKEN)
