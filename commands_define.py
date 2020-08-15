import random
import os
import praw
import discord

# !roll_dice command implementation
async def roll_dice(ctx):
    dice_roll_result = random.randint(1, 6) # get a random integer between 1 and 6
    if dice_roll_result == 1:
        path = os.path.join('gifs', 'Broj1.gif')
        desc=f"\nDice roll for *{ctx.author.name}:*\n **You got {dice_roll_result}** ! Shitty roll, kill yourself!"
    elif dice_roll_result == 2:
        path = os.path.join('gifs', 'Broj2.gif')
        desc=f"\nDice roll for *{ctx.author.name}:*\n **You got {dice_roll_result}** ! Not as shitty, but still die."
    elif dice_roll_result == 3:
        path = os.path.join('gifs', 'Broj3.gif')
        desc=f"\nDice roll for *{ctx.author.name}:*\n **You got {dice_roll_result}** ! Decent."
    elif dice_roll_result == 4:
        path = os.path.join('gifs', 'Broj4.gif')
        desc=f"\nDice roll for *{ctx.author.name}:*\n **You got {dice_roll_result}** ! Good one!"
    elif dice_roll_result == 5:
        path = os.path.join('gifs', 'Broj5.gif')           
        desc=f"\nDice roll for *{ctx.author.name}:*\n **You got {dice_roll_result}** ! Very nice!"
    else:
        path = os.path.join('gifs', 'Broj6.gif')
        desc=f"\nDice roll for *{ctx.author.name}:*\n **You got {dice_roll_result}** ! **Bravo!**" 
    file=discord.File(path, filename='image.gif')          
    embed=discord.Embed(title="Roll_dice Minigame", description=desc, color=0xfcfcfc)
    embed.set_thumbnail(url="attachment://image.gif")
    embed.set_footer(text="For more commands, type !help or !pomoc.")
    await ctx.send(file=file, embed=embed)


# deprecated implementation of dice_roll command
async def roll_dice_deprecated(ctx):
    dice_roll_result = random.randrange(1, 6) # get a random integer between 1 and 6
    await ctx.send(f"Dice roll for {ctx.author.name}: {dice_roll_result}")

async def print_help_message(ctx):
    msg="""```css
Commands:
    [1] !snake_game (not functioning)
    [2] !speed_typing (not functioning)
    [3] !roll_dice (Generates a random integer between 1 and 6)
    [4] !stupid (not functioning)
    [5] !play (not functioning)
    [6] !help (List of commands in English)
    [7] !pomoc (List of commands in Serbian)```"""
    await ctx.send(msg)

async def print_pomoc_message(ctx):
    msg = """```css
Komande:
    [1] !snake_game (ne funkcioniše)
    [2] !speed_typing (ne funkcioniše)
    [3] !roll_dice (Generise nasumican broj od 1 do 6)
    [4] !stupid (ne funkcioniše)
    [5] !play (ne funkcioniše)
    [6] !help (Lista komandi na engleskom)
    [7] !pomoc (Lista komandi na srpskom)```"""
    await ctx.send(msg)