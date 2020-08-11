import asyncio
import discord
import youtube_dl
from discord.ext import commands
import commands_define as cdef

# ENTER YOUR TOKEN HERE
TOKEN = "NzQxOTg2NzkyNTUwNjk0OTI0.Xy_jDA.u4J-VuCjjsUd6Rh-dpTONVeBas0"

client = commands.Bot(command_prefix="!")
client.remove_command('help')

# setup for music commands

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
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
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


# music commands

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await ctx.message.delete()
        await channel.connect()


    @commands.command()
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""

        await ctx.message.delete()
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    @commands.command()
    async def stupid(self, ctx, at=None):

        filename = "stupid_audio.m4a"
        if at is not None:
            await ctx.send(f"{at} is stupid!")
        await ctx.message.delete()
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(filename))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    @commands.command()
    async def yt(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""

        await ctx.message.delete()
        player = await YTDLSource.from_url(url, loop=self.client.loop)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)


    @commands.command()
    async def stream(self, ctx, *, url):
        """Streams from a url (same as yt, but doesn't predownload)"""

        await ctx.message.delete() 
        player = await YTDLSource.from_url(url, loop=self.client.loop, stream=True)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)


    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.message.delete()
        await ctx.voice_client.disconnect()

    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
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

    await ctx.message.delete()
    await cdef.roll_dice(ctx)

@client.command(pass_context=True)
async def roll_dice_deprecated(ctx):
    """Same as roll_dice, just basic text, no formating
        deprecated version """

    await ctx.message.delete()
    await cdef.roll_dice_deprecated(ctx)

@client.command(pass_context=True)
async def help(ctx):
    """prints command and what they do"""

    await ctx.message.delete()
    await cdef.print_help_message(ctx)

@client.command(pass_context=True)
async def pomoc(ctx):
    """prints help in Serbian language"""

    await ctx.message.delete()
    await cdef.print_pomoc_message(ctx)

@client.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('------')

client.add_cog(Music(client))
client.run(TOKEN)
