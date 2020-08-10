import random

# !roll_dice command implementation
async def roll_dice(message):
    dice_roll_result = random.randrange(1, 6) # get a random integer between 1 and 6
    await message.delete()
    await message.channel.send(f"Dice roll for {message.author.name}: {dice_roll_result}")
