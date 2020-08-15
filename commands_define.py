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
    [1]  !join <server> | tell bot to join voice server <voice_server>
    [2]  !addq <url>    | add song from url to music queue
    [3]  !pque          | start playing queue, if song is already playing skip it 
                        | (adds the bot to callers voice server if not already in voice server)
    [4]  !stop          | stop playing music and leave voice channel
    [5]  !roll_dice     | prints a random integer between 1 and 6
    [6]  !stupid (name) | starts a rant about how stupid last said thing is, 
                        | if name is given also tells given user that he is stupid
    [7]  !hot_meme      | prints the hottest meme from r/memes
    [8]  !rand_meme     | prints a random meme from r/memes
    [9]  !help          | list of commands in English
    [10] !pomoc         | list of commands in Serbian```"""
    await ctx.send(msg)

async def print_pomoc_message(ctx):
    msg = """```css
Komande:
    [1]  !join <kanal>  | naredi botu da se pridruzi glasovnom kanalu <kanal>
    [2]  !addq <link>   | dodaj pesmu sa linka u listu cekanja muzike
    [3]  !pque          | pocni da pustas listu pesama, preskoci pesmu ako je pustena 
                        | (dodaje bota u glasovni kanal onog koji je izdao komandu ako bot vec nije u glasovnom kanalu)
    [4]  !stop          | iskljuci muziku i napusti glasovni kanal
    [5]  !roll_dice     | ispisuje nasumican broj od 1 do 6
    [6]  !stupid (name) | pocinje da gundja o tome koliko je zadnja izgovorena stvar glupa, 
                        | ako je dato ime kao argument reci datom korisniku da je glup
    [7]  !hot_meme      | ispisuje trenutno najpopularniji mim iz r/memes
    [8]  !rand_meme     | daje nasumican mim iz r/memes
    [9]  !help          | lista komanda na engleskom
    [10] !pomoc         | lista komanda na srpskom```"""
    await ctx.send(msg)