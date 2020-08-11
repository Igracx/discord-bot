import random
import discord

# !roll_dice command implementation
async def roll_dice(ctx):
    dice_roll_result = random.randint(1, 6) # get a random integer between 1 and 6
    embed=discord.Embed(title="Roll_dice Minigame", description=f"\nDice roll for *{ctx.author.name}:*\n **You got {dice_roll_result}** ! Nice roll!", color=0xfcfcfc)
    embed.set_thumbnail(url="https://kcdd78689wordpress.files.wordpress.com/2019/02/dice-animation.gif")
    embed.set_footer(text="For more commands, type !help or !pomoc.")
    await ctx.send(embed=embed)

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