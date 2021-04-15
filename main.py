import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="!")
token = os.getenv("DISCORD_BOT_TOKEN")

@bot.event
async def on_ready():
        print('Le bot est allumé')

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
async def codecreateur(ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="Code Créateur",
                              description="Utilisez le code créateur SALVECKO pour soutenir Ecko!")
        embed.set_author(name="Ecko",
                         icon_url="https://cdn.discordapp.com/avatars/620340684150407179/6ee1539a66044b4ed216ea0826fa5a5e.png?size=128")
        embed.set_thumbnail(
                url="https://static-cdn.jtvnw.net/jtv_user_pictures/7cbf35e6-49de-4c76-81f3-52a9e63ae1e0-profile_image-70x70.png")
        embed.add_field(name="Code Créateur:", value="SALVECKO", inline=True)
        await ctx.send(embed=embed)

bot.run(token)
