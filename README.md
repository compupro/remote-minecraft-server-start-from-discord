# Remote Minecraft Server Start from Discord
A Discord bot that listens for a trigger phrase that will cause it to run a Minecraft server.

## Dependencies
* Python3 version **after** 3.8, because discord.py requires it.
* [discord.py](https://github.com/Rapptz/discord.py), the Discord API wrapper used. This bot has been tested on v1.7.3.

## Setup
Before running the bot from `bot_main.py`, you must set a few options in `settings.json`:
* `trigger_word`: the word or phrase you want the bot to look for to start the server.
* `server_jar_path`: the path to the server.jar file.
* `server_working_directory`: the place where you want all the server's files (e.g. map, server.properties, etc.) are.
* `bot_token`: the bot token you got from [Discord's "My Apps page"](https://discordapp.com/developers/applications/me)

On Windows devices you must use double backslashes in your file and directory paths. otherwise the slashes will be treated as escape characters.