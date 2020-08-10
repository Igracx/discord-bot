
# ENTER YOUR TOKEN HERE
TOKEN = "NzQxOTg2NzkyNTUwNjk0OTI0.Xy_jDA.x9pI1gN8WlbA1rk1IbY-zMZ-pUE"

import discord
import simple_game as sg

client = discord.Client()

def commands(command):
    if command == "!snake_game":
        # print("!snake_game")
        pass
    elif command == "!speed_typing":
        # print("!speed_typing")
        pass
    elif command == "!speed_typing_1v1":
        # print("!speed_typing_1v1")
        pass
    elif command == "!roll_dice":
        # print("!roll_dice")
        pass
    elif command == "!stupid":
        # print("!stupid")
        pass
    elif command == "!pic":
        # print("!pic")
        pass
    else:
        command_words = command.split()
        if len(command_words) != 2:
            # print("not 2")
            return
        if command_words[0] == "!play":
            # print("!play " + command_words[1])
            pass
        elif command_words[0] == "!is_stupid":
            # print("!is_stupid" + command_words[1])
            pass


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
        commands(message.content)

client.run(TOKEN)
