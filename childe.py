# base file from morgan @GoudaMorganing

import aiohttp						# Allows async commands
import discord						# Set status (presence)
import logging						# Enables logging for message counting
import io
import os							# Retrieve values from .env/Heroku
import random						# Randomize selection
import time							# Set cooldown interval
from discord.ext import commands	# For Discord bot
from quotes import *				# Import quotes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN 	= 'ODI3OTE2MzUxMDI0MDA1MTQw.YGh_MA.YGWuQHLdZZxBC6ksJ-X4T7ohkNM'  # TODO: Set the bot token
GUILD_ID 	= 823228184375853056

### ------------- ###
### BOT  SETTINGS ###
### ------------- ###

BOT_NAME			= 'Childe'  # TODO: Update your bot's name here!

# TODO: If you want to change any of their commands, update them accordingly
COMMAND_ABOUT 		= '?'
COMMAND_BIRTHDAY	= 'hb'
COMMAND_MORNING 	= 'gm'
COMMAND_EVENING		= 'ge'
COMMAND_NIGHT 		= 'gn'
COMMAND_INSULT 		= 'in'
COMMAND_CHAT		= 'ch'
COMMAND_CHOOSE		= 'choose'
COMMAND_RNG			= 'rng'

PREFIX 				= 'childe! '  # TODO: Changes the prefix of the bot (type abc! bd for birthday command)
PRESENCE			= 'with your life'  # TODO: Changes the bot's presence (Playing with Charmandie)

### ------------- ###
###   BOT VARS    ###
### ------------- ###

bot = commands.Bot(command_prefix = PREFIX, case_insensitive=True)

### ------------- ###
###     SETUP     ###
### ------------- ###

@bot.event
async def on_ready():
    GUILD = bot.get_guild(GUILD_ID)
    print(BOT_NAME + ' is connected to ' + str(GUILD) + '.')
    await bot.change_presence(activity=discord.Game(name=PRESENCE))

### ------------- ###
### MAIN COMMANDS ###
### ------------- ###

# ABOUT ٩(｡•́‿•̀｡)۶
@bot.command(name=COMMAND_ABOUT)
async def about(ctx):
    response = random.choice(quote_about)
    await ctx.send(response.format(ctx.author.display_name))

# BIRTHDAY _:(´ཀ`」 ∠):_
@bot.command(name=COMMAND_BIRTHDAY)
async def happyBirthday(ctx):
    response = random.choice(quote_birthday)
    await ctx.send(response.format(ctx.author.display_name))

# MORNING _:(´ཀ`」 ∠):_
@bot.command(name=COMMAND_MORNING)
async def goodMorning(ctx):
    response = random.choice(quote_morning)
    await ctx.send(response.format(ctx.author.display_name))

# EVENING _:(´ཀ`」 ∠):_
@bot.command(name=COMMAND_EVENING)
async def goodEvening(ctx):
    response = random.choice(quote_evening)
    await ctx.send(response.format(ctx.author.display_name))

# NIGHT (ﾉω･､)
@bot.command(name=COMMAND_NIGHT)
async def goodNight(ctx):
    response = random.choice(quote_night)
    await ctx.send(response.format(ctx.author.display_name))

# INSULT ▓▒░(°◡°)░▒▓
@bot.command(name=COMMAND_INSULT)
async def insult(ctx):
    response = random.choice(quote_insult)
    await ctx.send(response.format(ctx.author.display_name))

# CHAT (｡•́︿•̀｡)
@bot.command(name=COMMAND_CHAT)
async def chat(ctx):
    response = random.choice(quote_chat)
    await ctx.send(response.format(ctx.author.display_name))

@bot.command(name=COMMAND_CHOOSE)
async def choose(ctx, *, arg):
    arg_list = arg.split(' | ')
    response = 'Hmm... I choose ' + random.choice(arg_list) + '. What do you think, comrade?'
    if len(arg_list) == 1:
        response = 'Hah, very funny. I suppose I\'ll have to pick ' + arg_list[0] + '. Happy?'
    await ctx.send(response.format(ctx.author.display_name))

@choose.error
async def choose_error(ctx, error):
    if isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You aren\'t giving me much to work with. What am I choosing between?')

@bot.command(name=COMMAND_RNG)
async def rng(ctx, arg1, arg2):
    response = 'The lucky number is... ' + str(random.randint(int(arg1), int(arg2))) + '! Hope that helps with whatever.'
    await ctx.send(response.format(ctx.author.display_name))

@rng.error
async def rng_error(ctx, error):
    if isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You\'ll have to give me what numbers you want me to pick between first, comrade.')

bot.run(BOT_TOKEN)