
# <img src="https://raw.githubusercontent.com/RayNieport/mconBot/main/images/mcon.png" align="center" width="80"> mconBot

A bot to interact with your Minecraft server - from Discord! 

![DockerPulls](https://img.shields.io/docker/pulls/raynieport/mconbot?style=flat-square)
![DockerSize](https://img.shields.io/docker/image-size/raynieport/mconbot/arm64?style=flat-square)

__If you would like more customization, please see [the full docs](https://github.com/RayNieport/mconBot) on Github!__

## What exactly does mconBot do?

mconBot allows you and your friends to easily control your Minecraft server from the comfort of Discord!
Minecraft servers use a protocol called __[RCON](https://wiki.vg/RCON)__ to accept remote commands. If you're hosting your own server, you may have seen RCON mentioned in the server.properties file.

However, using RCON has some issues:
1. Port forwarding RCON to control your server over the internet is not very secure.
2. The RCON "user" has permission to run the full suite of Minecraft __[commands](https://minecraft.wiki/w/Commands)__, without any restrictions.
3. There is only one RCON "user", so your friends can't log in to moderate the server unless you give them the credentials for unrestricted RCON access.

To solve these problems, mconBot does the following:
1. Uses Discord as an interface to eliminate the need for port forwarding or a VPN (mconBot is intended to be hosted on the same LAN as your Minecraft server). 
2. Solves permission issues using a three-tiered system of Users, Moderators, and Administrators. Higher tiers allow more sensitive commands to be executed.


## Nice! How do I get started?

__First__, enable RCON by editing the __[server.properties](https://minecraft.wiki/w/Server.properties)__ file of your Minecraft server:
```
enable-rcon=true
rcon.password=<your passord>
rcon.port=25575
broadcast-rcon-to-ops=<optional, true|false>
```
__Second__, create your instance of the bot at the __[Discord Developer Portal](https://discord.com/developers/applications)__:
1. Click on the "New Application" button, and give your bot a name.
2. Give your bot a nice icon: the included icon is located __[here](https://raw.githubusercontent.com/RayNieport/mconBot/main/images/mcon.png)__.
3. Go to the Bot page and click "Add Bot".
4. Go to the OAuth2 page, scroll down to "Scopes", and select "bot". Under "Bot Permissions", select "View Channels" and "Send Messages".
5. Copy the link that was generated under "Scopes" and paste it into a new browser tab. Follow the instructions to add the bot to your Discord guild.
6. Head back to the Developer Portal and go to the Bot page. Uncheck "Public Bot", then copy the Token.

__Third__, modify __[this .env file](https://github.com/RayNieport/mconBot/blob/main/src/.env)__ and save it in a convenient directory on the computer running Docker:
1. Paste the Discord Token aquired above into the appropriate field.
2. Fill in your Minecraft server's IP and RCON password. If you're not using the default RCON port (25575), you can also change that.
3. Change the User, Mod, and Admin roles to the preffered roles in your Discord guild, or create the provided roles.

__Fourth__, head into the convenient directory you used above and run the docker image:
```
docker run -dt --name mconbot --env-file .env raynieport/mconbot
```
To specify the architecture, use `raynieport/mconbot:amd64` or `raynieport/mconbot:arm64`. Excluding a tag should automatically detect your machine's architecture and pull the appropriate image.

__Finally__, test out your bot by sending the following into a text channel in your Discord guild:
```
>hi
```
You should get the following response:

<img src="https://raw.githubusercontent.com/RayNieport/mconBot/main/images/hello.png">

For a list of all supported commands sorted by role, simply send the following:
```
>help
```

## Donate

If you enjoy mconBot, consider __[supporting my work](https://paypal.me/RayNieport)__ on this project and others! 

## License and Copyright

If you're interested in modifying or using my work for your own project, please see the __[LICENSE](https://github.com/RayNieport/mconBot/blob/main/LICENSE)__ for up to date copyright and license information regarding mconBot. Feel free to use my logo when hosting your own instance of mconBot. However, please don't use my logo for your own project without asking first - you can make your own Minecraft themed logo by creating a __[texture pack](https://minecraft.wiki/w/Tutorials/Creating_a_resource_pack)__ and rendering your modified asset using __[Block Renderer](https://www.curseforge.com/minecraft/mc-mods/block-renderer)__. If you have suggestions for my project or make your own derivative, I'd love to hear about it!
