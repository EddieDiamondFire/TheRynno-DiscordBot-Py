import discord
import os
import pathlib
from discord.ext import commands

class Main():


    discord_bot_client = commands.Bot(command_prefix = '!')
    bot_token_file_directory = str(pathlib.Path(__file__).parent.absolute()) + '\\data\\bot_token.txt'

    # File
    file_bot_token = open(bot_token_file_directory, "r")

    if not os.path.exists(bot_token_file_directory):
        print(" File does not exist, creating file")
        create_bot_token = open("bot_token.txt", "x")
        exit()
    else:
        if not os.path.getsize(bot_token_file_directory) > 0:
            print("There is no bot_token, please insert bot token in data/bot-token.txt")
            exit()


    print("Found bot token, initalizing sequence")

    @discord_bot_client.event
    async def on_ready():
        print("Discord Bot is ready")

    try:
        discord_bot_client.run(file_bot_token.read())
    except discord.LoginFailure:
        print("Error: Login Failed, Seems like you put an Invalid Bot Token in data/bot_token.txt")
        exit()

class Moderation():
