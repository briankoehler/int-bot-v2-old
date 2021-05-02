import os
import discord
import dotenv
from discord.ext import commands


# Initialize bot client
bot = commands.AutoShardedBot(command_prefix='?')


def setup_env():
	"""Get .env details from user input"""

	print('Thank you for using int bot.\nPlease provide the following details to setup the bot.  You can always change the .env file manually afterwards.')
	DISCORD_TOKEN = input('Enter your Discord bot token: ')
	RIOT_KEY = input('Enter your Riot API key: ')

	# Writing .env file
	with open('.env', 'w') as file:
		file.write('# .env\n\n')
		file.write(f'DISCORD_TOKEN="{DISCORD_TOKEN}"\n')
		file.write(f'RIOT_KEY="{RIOT_KEY}"\n')


@bot.command()
async def here(ctx: discord.ext.commands.Context):
	"""Set the notification channel to channel of command

	Args:
		ctx (discord.ext.commands.Context): Context of command
	"""

	...


@bot.event
async def on_guild_join(guild: discord.guild):
	"""Send a setup message to inviter

	Args:
		guild (discord.guild): Guild joined
	"""

	...


@bot.event
async def on_guild_remove(guild: discord.guild):
	"""Handle leaving a guild

	Args:
		guild (discord.guild): Guild left
	"""

	...



if __name__ == '__main__':

	# Checking if environment file exists
	if not os.path.isfile('.env'):
		setup_env()

	# Load environment variables
	dotenv.load_dotenv()
	DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
	RIOT_KEY = os.getenv('RIOT_KEY')

	# Run client
	bot.run(DISCORD_TOKEN)