# <img src="images/mcon.png" align="center" width="80"> mconBot

> A bot to interact with your Minecraft server - from Discord! 

[![DockerPulls](https://img.shields.io/docker/pulls/raynieport/mconbot?style=flat-square)](https://hub.docker.com/r/raynieport/mconbot)
[![LastCommit](https://img.shields.io/github/last-commit/RayNieport/mconBot?style=flat-square)](https://github.com/RayNieport/mconBot/commits/main)
[![License](https://img.shields.io/github/license/RayNieport/mconBot?style=flat-square)](https://github.com/RayNieport/mconBot/blob/main/LICENSE)


## What exactly does mconBot do?

mconBot allows you and your friends to easily control your Minecraft server from the comfort of Discord!
Minecraft servers use a protocol called __[RCON](https://wiki.vg/RCON)__ to accept remote commands. If you're hosting your own server, you may have seen RCON mentioned in the server.properties file.

However, using RCON has some issues:
1. Port forwarding RCON to control your server over the internet is not very secure.
2. The RCON "user" has permission to run the full suite of Minecraft __[commands](https://minecraft.fandom.com/wiki/Commands)__, without any restrictions.
3. There is only one RCON "user", so your friends can't log in to moderate the server unless you give them the credentials for unrestricted RCON access.

To solve these problems, mconBot does the following:
1. Uses Discord as an interface to eliminate the need for port forwarding or a VPN (mconBot is intended to be hosted on the same LAN as your Minecraft server). 
2. Solves permission issues using a three-tiered system of Users, Moderators, and Administrators. Higher tiers allow more sensitive commands to be executed.

><img src="images/mconBotDemo.png" width="1000">

## Nice! How do I get started?

__For a simple pre-built docker image, follow the guide on [Docker Hub](https://hub.docker.com/r/raynieport/mconbot). Otherwise, proceed with manual installation:__

__First__, enable RCON by editing the __[server.properties](https://minecraft.fandom.com/wiki/Server.properties)__ file of your Minecraft server:
```
enable-rcon=true
rcon.password=<your passord>
rcon.port=25575
broadcast-rcon-to-ops=<optional, true|false>
```
__Second__, clone the git respository to the machine you want to run the bot on:
```
git clone https://github.com/RayNieport/mconBot.git
```

__Third__, install __[python 3](https://www.python.org/downloads/)__ , then navigate to the cloned repository and install the necessary dependencies:
```
pip3 install -r requirements.txt
```

__Fourth__, create your instance of the bot at the __[Discord Developer Portal](https://discord.com/developers/applications)__:
1. Click on the "New Application" button, and give your bot a name.
2. Give your bot a nice icon: the included icon is located at mconBot/images/mcon.png in the cloned repository.
3. Go to the Bot page and click "Add Bot".
4. Go to the OAuth2 page, scroll down to "Scopes", and select "bot". Under "Bot Permissions", select "View Channels" and "Send Messages".
5. Copy the link that was generated under "Scopes" and paste it into a new browser tab. Follow the instructions to add the bot to your Discord guild.
6. Head back to the Developer Portal and go to the Bot page. Uncheck "Public Bot", then copy the Token.

__Fifth__, modify __mconBot/src/.env__ in the cloned repository:
1. Paste the Discord Token aquired above into the appropriate field.
2. Fill in your Minecraft server's IP and RCON password.
3. Change the User, Mod, and Admin roles to the preffered roles in your Discord guild, or create the provided roles.

__Sixth__, head into __/mconBot/src/__ in the cloned repository and start up the bot:
```
python3 mconBot.py
```
__Finally__, test out your bot by sending the following into a text channel in your Discord guild:
```
>hi
```
You should get the following response:

<img src="images/hello.png">

For a list of all supported commands sorted by role, simply send the following:
```
>help
```

## What else is included in this repository?
1. If you're interested in running mconBot as a Docker container, the included __Dockerfile__ and __requirements.txt__ will allow you to build the image. I recommend running through all the steps above to test your bot before building the image.
2. If you want to modify which roles have access to certain commands, you can modify __mconBot/src/commands.json__. You should be able to add extra commands here as well, although this is not officially supported.
3. The __mconBot/mcon_pack/__ directory is a minecraft texture pack with modified furnace texture. This was used to generate the logo for the project. You can use this texture pack as an example if you want to create a custom minecraft-themed logo. For more info on creating your own logo, see the Licencse and Copyright section below.

## Donate

If you enjoy mconBot, consider __[supporting my work](https://paypal.me/RayNieport)__ on this project and others! 

## License and Copyright

If you're interested in modifying or using my work for your own project, please see the LICENSE for up to date copyright and license information regarding mconBot. Please don't use my logo without asking first - you can make your own Minecraft themed logo by creating a __[texture pack](https://minecraft.fandom.com/wiki/Tutorials/Creating_a_resource_pack)__ and rendering your modified asset using __[Block Renderer](https://www.curseforge.com/minecraft/mc-mods/block-renderer)__. If you have suggestions for my project or make your own derivative, I'd love to hear about it!
