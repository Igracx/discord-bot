import random

# !roll_dice command implementation
async def roll_dice(message):
    dice_roll_result = random.randrange(1, 6) # get a random integer between 1 and 6
    await message.delete()
    await message.channel.send(f"Dice roll for {message.author.name}: {dice_roll_result}")

async def print_help_message(message):
	await message.channel.send(f'```css\nList of commands:\n [1] !snake_game (not functioning)\n [2] !roll_dice (Generates a random integer between 1 and 6)\n [3] !stupid (not functioning)\n [4] !speed_typing (not functioning)\n [5] !play (not functioning)\n [6] !pomoc (Serbian command-list)\n ```')
