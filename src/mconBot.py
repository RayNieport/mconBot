# mconBot.py
# Ray Nieport 2021

import os
import json
import discord
from dotenv import load_dotenv
from mcrcon import MCRcon

# Get environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USER_ROLE = os.getenv('DISCORD_USER_ROLE')
MOD_ROLE = os.getenv('DISCORD_MOD_ROLE')
ADMIN_ROLE = os.getenv('DISCORD_ADMIN_ROLE')
IP = os.getenv('MINECRAFT_IP')
PASS = os.getenv('MINECRAFT_PASS')

# Get dictionary of commands
with open('commands.json') as cmd_file:
    cmds = json.load(cmd_file)

# Create help message
Help = discord.Embed(description="A bot to interact with your Minecraft server - from Discord!")
Help.add_field(name='\u200b', value='-------------------------' + USER_ROLE + '-------------------------')
for com in cmds['user_commands']:
    Help.add_field(name=com, value=cmds['user_commands'][com], inline=False)
Help.add_field(name='\u200b', value='-------------------------' + MOD_ROLE + '-------------------------')
for com in cmds['mod_commands']:
    Help.add_field(name=com, value=cmds['mod_commands'][com], inline=False)
Help.add_field(name='\u200b', value='-------------------------' + ADMIN_ROLE + '-------------------------')
for com in cmds['admin_commands']:
    Help.add_field(name=com, value=cmds['admin_commands'][com], inline=False)

# Send command via rcon and print response
async def send_rcon(cmd, args, message):
    try:
        with MCRcon(IP, PASS) as mcr:
            resp = mcr.command(cmd + ' ' + args)
    except:
        resp = 'Connection from the bot to the server failed.'

    print (f'[{message.author}]: {cmd} {args}')
    if resp:
        await message.channel.send(resp)
        print (f'{resp}')

# When message received
bot = discord.Client()
@bot.event
async def on_message(message):
    if not message.content.startswith('>') or message.author == bot.user:
        return

    # get command and arguments
    try:
        cmd, args = message.content[+1:].split(None, 1)
    except:
        cmd = message.content[+1:]
        args = ''

    # get author's clearance level
    authLevel = 0
    for role in message.author.roles:
        if role.name == USER_ROLE: authLevel+=1
        elif role.name == MOD_ROLE: authLevel+=2
        elif role.name == ADMIN_ROLE: authLevel+=4

    # handle command
    if cmd == 'help':
        await message.channel.send(embed=Help)
    elif cmd == 'hi':
        await message.channel.send('Hello! I\'m the Minecraft RCON bot!')
        print (f'Said hi to {message.author}.')
    elif cmd in cmds['user_commands']:
        if authLevel >= 1:
            await send_rcon(cmd, args, message)
        else:
            await message.channel.send('Sorry, you need the ' + USER_ROLE + ' role to use that command.')
    elif cmd in cmds['mod_commands']:
        if authLevel >= 2:
            await send_rcon(cmd, args, message)
        else:
            await message.channel.send('Sorry, you need the ' + MOD_ROLE + ' role to use that command.')
    elif cmd in cmds['admin_commands']:
        if authLevel >= 4:
            await send_rcon(cmd, args, message)
        else:
            await message.channel.send('Sorry, you need the ' + ADMIN_ROLE + ' role to use that command.')
    else:
        await message.channel.send('Invalid command.')

bot.run(TOKEN)