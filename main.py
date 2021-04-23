import discord
from discord.ext import commands
import os
import json
warnings = {}



token = os.getenv("DISCORD_BOT_TOKEN")
intents = discord.Intents.default()
intents.members = True
guild_subscriptions = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print('Le bot est allumé')
    await bot.change_presence(activity=discord.Streaming(name="SalvEcko", url="https://www.twitch.tv/salvecko"))

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
