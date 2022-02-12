# mconBot.py
# Ray Nieport 2021

import discord
from rcon import rcon
from os import getenv
from dotenv import load_dotenv
from json import load

# Override default Client class to allow messages from other bots
class UnfilteredClient(discord.Client):
    async def process_commands(self, message):
        ctx = await self.get_context(message)
        await self.invoke(ctx)

client = UnfilteredClient()

if __name__ == "__main__":
    # Get environment variables
    load_dotenv()
    TOKEN = getenv('DISCORD_TOKEN')
    USER_ROLE = getenv('DISCORD_USER_ROLE')
    MOD_ROLE = getenv('DISCORD_MOD_ROLE')
    ADMIN_ROLE = getenv('DISCORD_ADMIN_ROLE')
    IP = getenv('MINECRAFT_IP')
    PASS = getenv('MINECRAFT_PASS')
    PORT = getenv('RCON_PORT')
    BOT_LEVEL = getenv('BOT_LEVEL')
    if PORT == None: PORT = 25575
    else: PORT = int(PORT)
    if BOT_LEVEL == None: BOT_LEVEL = 1
    else: BOT_LEVEL = int(BOT_LEVEL) 

    # Get dictionary of commands
    with open('commands.json') as cmd_file:
        cmds = load(cmd_file)

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
    Help.add_field(name='admin', value='Runs a custom command', inline=False)


# Send command via rcon and print response
async def send_rcon(cmd, args, message):
    try:
        with rcon(IP, PASS, PORT) as mcr:
            if args:
                resp = mcr.command(cmd + ' ' + args)
            else:
                resp = mcr.command(cmd)
    except:
        resp = 'Connection from the bot to the server failed.'

    print (f'[{message.author}]: {cmd} {args}')
    if resp:
        await message.channel.send(resp)
        print (f'{resp}')


# Process message when received
@client.event
async def on_message(message):
    if not message.content.startswith('>') or message.author == client.user:
        return

    # get command and arguments
    try:
        cmd, args = message.content[+1:].split(None, 1)
    except:
        cmd = message.content[+1:]
        args = ''

    # get author's clearance level
    authLevel = 0
    if message.author.bot == 1:
        authLevel = BOT_LEVEL
    else:
        for role in message.author.roles:
            if role.name == USER_ROLE: authLevel+=1
            elif role.name == MOD_ROLE: authLevel+=2
            elif role.name == ADMIN_ROLE: authLevel+=4

    # handle command
    if cmd == 'help':
        await message.channel.send(embed=Help)
        print (f'Helped out {message.author}.')
    elif cmd == 'hi':
        await message.channel.send('Hello! I\'m the Minecraft RCON bot!')
        print (f'Said hi to {message.author}.')
    elif cmd == 'admin':
        if authLevel >= 4:
            cmd = args
            args = ''
            await send_rcon(cmd, args, message)
        else:
            await message.channel.send('Sorry, you need the ' + ADMIN_ROLE + ' role to use that command.')
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

client.run(TOKEN)
