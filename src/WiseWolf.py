import discord
import sys
import signal
import asyncio
from discord.ext import commands
import Database_helpers

bot = commands.Bot(command_prefix='!ww ')
token = ''
extentions = []

def signal_handler(signal, frame):
    '''(Signal, Frame) -> null
    Upon signal, stop the bot and exit the program
    '''

    print("\nLogging out bot...")
    leave_all_voice_channels(bot)
    # log out bot and close connection
    bot.logout()
    bot.close()
    print("Bot has logged out.")
    # exit program
    sys.exit(0)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(bot.guilds[0].id)
    print('------')
    # Database_helpers.initialize(str(bot.guilds[0].id))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message : str):
    banned = ['owo']

    try:
        if any(s in message.content for s in banned):
            await message.channel.send("YOU ARE BANNED")
    except commands.errors.CommandNotFound:
        await bot.say("command not supported")

modules = ["WaifuGacha"]

if (__name__ == "__main__"):
    # amount of arguments
    argc = len(sys.argv)
    # bot token
    token = None

    # map Ctrl+C to trigger signal_handler function
    signal.signal(signal.SIGINT, signal_handler)

    print("Logging in...")

    # parse command line arguments
    for i in range(argc):
        if (sys.argv[i] == "-t" and i < argc):
            token = sys.argv[i+1]
    if (token is None):
        print("Error: no token given")
        sys.exit(1)
    for module in modules:
        bot.load_extension(module)
    bot.run(token)
