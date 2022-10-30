import discord
import os
import json
import asyncio
import threading

intents = discord.Intents.default()

#load the settings
with open('settings.json', 'r') as settings_file:
    settings_json = settings_file.read()
    settings_file.close()
    bot_settings = json.loads(settings_json)

#set up the bot
os.chdir(bot_settings['server_working_directory'])
bot = discord.Client(intents=intents)
server_thread = None

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='without a server.'))
    print("Bot service started successfully.")
    
@bot.event
async def on_message(message):
    global server_thread
    if message.content == bot_settings['trigger_word']:
        
        try:
            if not server_thread.is_alive(): server_thread = None
        except AttributeError: #will update server_thread to None if there is no server thread, just in case.
            server_thread = None
            
        if server_thread == None:
            await message.channel.send("Starting Minecraft server.")
            print("{} (ID {}) started the Minecraft server.".format(message.author.display_name, message.author.id))
            start_server = lambda: os.system('java -jar ' + bot_settings['server_jar_path'])
            server_thread = threading.Thread(target=start_server)
            server_thread.start()
            await bot.change_presence(activity=discord.Game(name='with a server.'))
            print("Minecraft server started successfully.")
        else:
            await message.channel.send("Minecraft server already running!")
            
#run the bot
bot.run(bot_settings['bot_token'])
