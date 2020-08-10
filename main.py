import commands

# ENTER YOUR TOKEN HERE
TOKEN = "NTI4OTY4MDM4NzcxNDU4MDcz.XCjt4A.3tmFi1kF-Qotn5GAh5DKMKm5Qmo"

import discord
import simple_game as sg
import commands

client = discord.Client()

@client.event # event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")
    # print_help_message() # NAPRAVI FUNKCIJU U NOVOM FAJLU ZA OVO

@client.event
async def on_message(message):
    # print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")  # MISLIM DA NAM OVO NE TREBA
    if message.author == client.user or message.content == '':
        return
    if message.content[0] == "!":
        if message.content == "!snake_game":
            # print("!snake_game")
            pass
        elif message.content == "!speed_typing":
            # print("!speed_typing")
            pass
        elif message.content == "!speed_typing_1v1":
            # print("!speed_typing_1v1")
            pass
        elif message.content == "!roll_dice":
            await commands.roll_dice(message)

        elif message.content == "!stupid":
            # print("!stupid")
            pass
        elif message.content == "!pic":
            # print("!pic")
            pass
        elif message.content == "!help":
            await commands.print_help_message(message)    
        elif message.content == "!pomoc":
            await message.channel.send(f'```css\nLista komandi:\n [1] !snake_game (ne funkcioniše)\n [2] !roll_dice (Generise nasumican broj od 1 do 6)\n [3] !stupid (ne funkcioniše)\n [4] !speed_typing (ne funkcioniše)\n [5] !play (ne funkcioniše)\n [6] !help (Lista komandi na engleskom)\n ```')    
        else:
            command_words = message_content.split()
            if len(command_words) != 2:
                # print("not 2")
                return
            if command_words[0] == "!play":
                # print("!play " + command_words[1])
                pass
            elif command_words[0] == "!is_stupid":
                # print("!is_stupid" + command_words[1])
                pass

client.run(TOKEN)
