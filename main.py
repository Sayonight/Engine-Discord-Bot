import discord
from discord.ext import commands
import os
from webserver import keep_alive

from Cardmarket import getData, insertData
from PasswordGen import generate_password

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
client.remove_command("help")


#Start anzeige
@client.event
async def on_ready():
  print('We have logged on as user {0.user}'.format(client))


#Ping test
@client.command()
async def ping(ctx):
  await ctx.reply("Pong!")


#Add Links to Cardmarket
@client.command()
async def addLink(ctx, link):
  insertData(link)
  await ctx.send("eingefügt")


#Passwort Generation
@client.command(name="pw")
async def genPasswort(ctx):
  await ctx.send(generate_password())
  await ctx.send(generate_password())
  await ctx.send(generate_password())


#Show Card Value
@client.command(name="sv")
async def showCardValue(ctx):
  await ctx.send(getData())


keep_alive()
client.run(os.environ['TOKEN'], reconnect=True)
