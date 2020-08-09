# id 741986792550694924
# token NzQxOTg2NzkyNTUwNjk0OTI0.Xy_jDA.5djV-CWB2ypze8SAwCXgKvRDxPQ
# permisions integer 67648
# https://discordapp.com/oauth2/authorize?client_id=741986792550694924&scope=bot&permissions=67648

import discord
import simple_game as sg

client = discord.Client()

def build_screen(O_POS):
    line = 'X'*SCREEN_WIDTH
    msg = (line + '\n') * SCREEN_HEIGHT
    return msg


@client.event # event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    # print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if message.author == client.user:
        return

    if message.content[0] == '!':
        if message.content[1:] == 'play_game':
            await message.channel.send('simple game\n' + '```' + sg.msg() + '```' )

client.run("NzQxOTg2NzkyNTUwNjk0OTI0.Xy_jDA.5djV-CWB2ypze8SAwCXgKvRDxPQ")
