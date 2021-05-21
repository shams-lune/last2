import discord
from discord.ext import commands
import os
import json
import requests
import requests
import json
import sys
from twitchAPI.twitch import Twitch
import os
import json
import discord
import requests
from discord.ext import tasks, commands
from twitchAPI.twitch import Twitch
from discord.utils import get
import time


token = os.getenv("DISCORD_BOT_TOKEN")
header = os.getenv("API_KEY")
intents = discord.Intents.default()
intents.members = True
guild_subscriptions = True
bot = commands.Bot(command_prefix="!", intents=intents)

client_id = "ksfaak3qm1po2lva4rbteotitqqel4"
client_secret = "rwbehbkk6z7b0zxyi3parc8phcc2hj"
twitch = Twitch(client_id, client_secret)
twitch.authenticate_app([])
TWITCH_STREAM_API_ENDPOINT_V5 = "https://api.twitch.tv/kraken/streams/{}"
API_HEADERS = {
    'Client-ID': client_id,
    'Accept': 'application/vnd.twitchtv.v5+json',
}

response  = requests.get("https://api.twitch.tv/kraken/streams/", headers=API_HEADERS)
response_json = response.json()

userid = twitch.get_users(logins=['SalvEcko'])['data'][0]['id']
url = TWITCH_STREAM_API_ENDPOINT_V5.format(userid)
req = requests.Session().get(url, headers=API_HEADERS)
jsondata = req.json()
print(jsondata['stream'])

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)
#cd C:\Users\mtagd\OneDrive\Bureau

game = jsondata['stream']['channel']['status']

@bot.command()
async def a(ctx, arg1, arg2):
    plateform = arg1
    nom_du_joueur = arg2
    r = requests.get(url="https://public-api.tracker.gg/v2/apex/standard/profile/"+ plateform + "/" + nom_du_joueur, headers={"TRN-Api-Key":"16e7d718-8c74-4146-be31-8c31cf8ada29"})
    data = r.json()

    if arg1 == "origin":
        embed=discord.Embed(title="**Stats pour** " +arg2+ " **[PC]**", colour=0xff0000)
        embed.add_field(name="**Level:**", value=data['data']['segments'][0]['stats']['level']['displayValue'])
        embed.add_field(name="**Rank:**", value=data['data']['segments'][0]['stats']['rankScore']['metadata']['rankName'])
        embed.add_field(name="**Rank Score:**", value=data['data']['segments'][0]['stats']['rankScore']['value'])
        embed.add_field(name="**Kills:**", value=data['data']['segments'][0]['stats']['kills']['displayValue'])
        embed.add_field(name="Légende actuelle:", value=data['data']['segments'][1]['metadata']['name'])
        embed.set_thumbnail(url=data['data']['segments'][1]['metadata']['imageUrl'])
        embed.set_author(name=arg2, icon_url=data['data']['platformInfo']['avatarUrl'])
        embed.set_image(url=f"{data['data']['segments'][0]['stats']['rankScore']['metadata']['iconUrl']}")
        embed.set_footer(text="Par ! 𝕁𝕠𝕜𝕖𝕣#5236, api : tracker.gg", icon_url="https://cdn.discordapp.com/avatars/658714497778974762/806ca93cc1711a4023a127d680691598.png?size=128")
        embed.add_field(name="Kill avec "+ data['data']['segments'][1]['metadata']['name'], value=arg2+" à fait " + data['data']['segments'][0]['stats']['kills']['displayValue']+ " kills avec " + data['data']['segments'][1]['metadata']['name'])
        embed.add_field(name="Kill avec " + data['data']['segments'][2]['metadata']['name'], value=arg2+" à fait " + data['data']['segments'][0]['stats']['kills']['displayValue'] + ' kills avec '+ data['data']['segments'][2]['metadata']['name'])
        embed.add_field(name="Plus d'info sur :", value="https://apex.tracker.gg/apex/profile/"+ arg1 +"/"+arg2+"/overview", inline=False)

        await ctx.send(embed=embed)

    if arg1 == "psn":
        embed = discord.Embed(title="**Stats pour** " + arg2 + " **[PLAYSTATION]**", colour=0xff0000)
        embed.add_field(name="**Level:**", value=data['data']['segments'][0]['stats']['level']['displayValue'])
        embed.add_field(name="**Rank:**",
                        value=data['data']['segments'][0]['stats']['rankScore']['metadata']['rankName'])
        embed.add_field(name="**Rank Score:**", value=data['data']['segments'][0]['stats']['rankScore']['value'])
        embed.add_field(name="**Kills:**", value=data['data']['segments'][0]['stats']['kills']['displayValue'])
        embed.add_field(name="Légende actuelle:", value=data['data']['segments'][1]['metadata']['name'])
        embed.set_thumbnail(url=data['data']['segments'][1]['metadata']['imageUrl'])
        embed.set_author(name=arg2, icon_url=data['data']['platformInfo']['avatarUrl'])
        embed.set_image(url=f"{data['data']['segments'][0]['stats']['rankScore']['metadata']['iconUrl']}")
        embed.set_footer(text="Par ! 𝕁𝕠𝕜𝕖𝕣#5236, api : tracker.gg",
                         icon_url="https://cdn.discordapp.com/avatars/658714497778974762/806ca93cc1711a4023a127d680691598.png?size=128")
        embed.add_field(name="Kill avec " + data['data']['segments'][1]['metadata']['name'],
                        value=arg2 + " à fait " + data['data']['segments'][0]['stats']['kills'][
                            'displayValue'] + " kills avec " + data['data']['segments'][1]['metadata']['name'])
        embed.add_field(name="Kill avec " + data['data']['segments'][2]['metadata']['name'],
                        value=arg2 + " à fait " + data['data']['segments'][0]['stats']['kills'][
                            'displayValue'] + ' kills avec ' + data['data']['segments'][2]['metadata']['name'])
        embed.add_field(name="Plus d'info sur :",
                        value="https://apex.tracker.gg/apex/profile/" + arg1 + "/" + arg2 + "/overview", inline=False)

        await ctx.send(embed=embed)


    if arg1 == "xbl":
        embed = discord.Embed(title="**Stats pour** " + arg2 + " **[XBOX]**", colour=0xff0000)
        embed.add_field(name="**Level:**", value=data['data']['segments'][0]['stats']['level']['displayValue'])
        embed.add_field(name="**Rank:**",
                        value=data['data']['segments'][0]['stats']['rankScore']['metadata']['rankName'])
        embed.add_field(name="**Rank Score:**", value=data['data']['segments'][0]['stats']['rankScore']['value'])
        embed.add_field(name="**Kills:**", value=data['data']['segments'][0]['stats']['kills']['displayValue'])
        embed.add_field(name="Légende actuelle:", value=data['data']['segments'][1]['metadata']['name'])
        embed.set_thumbnail(url=data['data']['segments'][1]['metadata']['imageUrl'])
        embed.set_author(name=arg2, icon_url=data['data']['platformInfo']['avatarUrl'])
        embed.set_image(url=f"{data['data']['segments'][0]['stats']['rankScore']['metadata']['iconUrl']}")
        embed.set_footer(text="Par ! 𝕁𝕠𝕜𝕖𝕣#5236, api : tracker.gg",
                         icon_url="https://cdn.discordapp.com/avatars/658714497778974762/806ca93cc1711a4023a127d680691598.png?size=128")
        embed.add_field(name="Kill avec " + data['data']['segments'][1]['metadata']['name'],
                        value=arg2 + " à fait " + data['data']['segments'][0]['stats']['kills'][
                            'displayValue'] + " kills avec " + data['data']['segments'][1]['metadata']['name'])
        embed.add_field(name="Kill avec " + data['data']['segments'][2]['metadata']['name'],
                        value=arg2 + " à fait " + data['data']['segments'][0]['stats']['kills'][
                            'displayValue'] + ' kills avec ' + data['data']['segments'][2]['metadata']['name'])
        embed.add_field(name="Plus d'info sur :",
                        value="https://apex.tracker.gg/apex/profile/" + arg1 + "/" + arg2 + "/overview", inline=False)

        await ctx.send(embed=embed)


@a.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Le joueur que vous essayez de chercher n'a pas été trouver ! Veuillez rentrer !apex plateform(origin pour pc, psn pour playstation, xbl pour xbox) et son identifiant !")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Veuillez rentrer !apex plateform(origin pour pc, psn pour playstation, xbl pour xbox) et son identifiant !")

@bot.event
async def on_ready():
    print('Le bot est allumé')
    await bot.change_presence(activity=discord.Streaming(name="SalvEcko", url="https://www.twitch.tv/salvecko"))
    while 1+1 != 0: 
		if jsondata['stream'] is not None:
			channel = bot.get_channel(845353988165206087)
			embed=discord.Embed(title=f"{jsondata['stream']['channel']['status']}", url=f"{jsondata['stream']['channel']['url']}", color=0x02dd08)
			embed.set_author(name="SalvEcko is now live on Twitch!", url=f"{jsondata['stream']['channel']['url']}", icon_url=f"{jsondata['stream']['channel']['logo']}")
			embed.add_field(name=f"Playing {jsondata['stream']['channel']['game']} for {jsondata['stream']['viewers']} viewers", value=f"[Watch Stream]({jsondata['stream']['channel']['url']})",inline=True)
			embed.set_image(url=f"{jsondata['stream']['preview']['large']}")
			await channel.send(f"@everyone {jsondata['stream']['channel']['status']}\n{jsondata['stream']['channel']['url']}\n", embed=embed)
			break
		elif game is not jsondata['stream']['channel']['status']:
			embed=discord.Embed(title=f"{jsondata['stream']['channel']['status']}", url=f"{jsondata['stream']['channel']['url']}", color=0x02dd08)
			embed.set_author(name="SalvEcko is now live on Twitch!", url=f"{jsondata['stream']['channel']['url']}", icon_url=f"{jsondata['stream']['channel']['logo']}")
			embed.add_field(name=f"Playing {jsondata['stream']['channel']['game']} for {jsondata['stream']['viewers']} viewers", value=f"[Watch Stream]({jsondata['stream']['channel']['url']})",inline=True)
			embed.set_image(url=f"{jsondata['stream']['preview']['large']}")
			embed.set_thumbnail(url=f"{jsondata['stream']['channel']['url']}")
			await channel.send(f"@everyone {jsondata['stream']['channel']['status']}\n{jsondata['stream']['channel']['url']}\n", embed=embed)
			break
		else:
			continue

@bot.listen()
async def on_message(message):
    if "neige" in message.content.lower():
        await message.channel.send('❄🌨❄🌨')
        await bot.process_commands(message)
    if "ekip" in message.content.lower():
        await message.add_reaction(":ekip112:762297421044121611")
    if "bonjour" in message.content.lower():
        await message.add_reaction(":SalveckOY:740928694855663799")
    if "oy" in message.content.lower():
        await message.add_reaction(":SalveckOY:740928694855663799")
    if "hey" in message.content.lower():
        await message.add_reaction(":SalveckOY:740928694855663799")
    if "salut" in message.content.lower():
        await message.add_reaction(":SalveckOY:740928694855663799")
    if "bonsoir" in message.content.lower():
        await message.add_reaction(":SalveckOY:740928694855663799")
    if "bonjoir" in message.content.lower():
        await message.add_reaction(":SalveckOY:740928694855663799")
    if "bijoir" in message.content.lower():
        await message.add_reaction(":SalveckOY:740928694855663799")
    if "oy" in message.content.lower():
        await message.add_reaction(":SalveckOY:740928694855663799")
    if ":SalveckOY:740928694855663799" in message.content.lower():
        await message.add_reaction(":SalveckOY:740928694855663799")
    if ":ekip112:762297421044121611" in message.content.lower():
        await message.add_reaction(":ekip112:762297421044121611")
	    

@bot.command()
async def oyshop(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Oy Shop", url="https://www.oyshop.fr/", description="Le Oy shop est le shop de Ecko vous pouvez y trouver plein de vêtements de très bonne qualité", color=0xffffff)
    embed.set_author(name="Shop Ecko", url="https://www.oyshop.fr/", icon_url="https://assets.bigcartel.com/theme_images/56559731/logo2OY.png?auto=format&fit=max&h=240&w=1000")
    embed.set_thumbnail(url="https://assets.bigcartel.com/theme_images/56559731/logo2OY.png?auto=format&fit=max&h=240&w=1000")
    embed.add_field(name="Lien du Oy Shop:", value="https://www.oyshop.fr/", inline=True)
    embed.set_footer(text="Oy shop")
    await ctx.send(embed=embed)

@bot.command()
async def mc(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Minecraft FTB infinty involved", url="https://www.feed-the-beast.com/", description="(Cliquez sur le message au dessus pour télécharger le launcher)", color=0x37ff00)
    embed.set_author(name="Epithut", icon_url="https://cdn.discordapp.com/avatars/539582678727393302/3333f80894f164eaec05e5bc2760adaf.png?size=128")
    embed.add_field(name="Serveur minecraft FTB infinty involved ouvert à tous :", value="ip: 51.254.81.62:27110", inline=False)
    embed.add_field(name="Règles:", value="Règles: - respecter les autres joueurs que ce sois dans le chat ou en jeux  - le vole ou la destruction volontaire est interdite - je m'octroie le droit de ban toute personne ne respectant pas ces règles (je paye après tout le serveur ahah) pour nous rejoindre", inline=False)
    embed.add_field(name="Pour nous rejoindre:", value='Télécharger le launcher -> https://www.feed-the-beast.com/ Ensuite dans celui si dans la section "browse" taper "FTB infity evolved" et cliquer dessus (pas infinty avolved skyblock mais l autre) une fois télécharger lancer le jeux connecter vous avec votre compte minecraft aller dans multiplayer et faite "Add server" ou "Nouveau serveur" et mettez l ip si dessus ', inline=False)
    embed.set_footer(text="Bon jeux à tous :)")
    await ctx.send(embed=embed)

@bot.command()
async def codecreateur(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Code Créateur",
                              description="Utilisez le code créateur SALVECKO pour soutenir Ecko!")
    embed.set_author(name="Ecko",
                         icon_url="https://cdn.discordapp.com/avatars/620340684150407179/6ee1539a66044b4ed216ea0826fa5a5e.png?size=128")
    embed.set_thumbnail(
                url="https://static-cdn.jtvnw.net/jtv_user_pictures/7cbf35e6-49de-4c76-81f3-52a9e63ae1e0-profile_image-70x70.png")
    embed.add_field(name="Code Créateur:", value="SALVECKO", inline=True)
    embed.add_field(name="Tuto de comment mettre le code créateur:", value="https://clips.twitch.tv/CulturedResourcefulNuggetsFutureMan-JrAs4TWCyd33Fbll", inline=True)
    await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
    print("Quelqu'un a rejoins")
    channel = bot.get_channel(683769890888351811)
    embed=discord.Embed(title="Bienvenue", url="https://www.twitch.tv/salvecko", description="Tout le monde te souhaite la bienvenue dans l'**Ekip**", color=0xffffff)
    embed.set_author(name=f"Bienvenue {member.display_name} !!", url="https://www.twitch.tv/salvecko", icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/7cbf35e6-49de-4c76-81f3-52a9e63ae1e0-profile_image-70x70.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/762297421044121611.png?v=1")
    await channel.send(embed=embed, delete_after=300.0)
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user: discord.User, *, reason="Aucune raison n'a été donné"):
    await ctx.message.delete()
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")
    # await ctx.guild.ban(user, reason = reason)
    embed = discord.Embed(title="**Banissement**", description="Un modérateur a frappé !",
                          url="https://www.youtube.com/channel/UChDVo_Uqomuk7KnMVp-Lhhw?view_as=subscriber",
                          color=0x423A80)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url,
                     url="https://www.youtube.com/channel/UChDVo_Uqomuk7KnMVp-Lhhw?view_as=subscriber")
    embed.set_thumbnail(url="https://discordemoji.com/assets/emoji/BanneHammer.png")
    embed.add_field(name="Membre banni", value=user.name, inline=True)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.add_field(name="Modérateur", value=ctx.author.name, inline=True)
    embed.set_footer(text=random.choice(funFact))

    await ctx.send(embed=embed)



@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx,
				user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} à été unban.")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"{user} à été kick.")


@bot.command()
async def clear(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre + 1).flatten()
	for message in messages:
		await message.delete()
bot.run(token)
