import discord
import lvlsys
# import spamdet
# import dice
from discord.ext import commands

cogs = [lvlsys] #add spamdet and dice back

client = commands.Bot(command_prefix="+", intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("ODA3MTQ3OTEwNzY0MDM2MTI3.YBzxEg.f14RU19hAwM8IRGNIT0CxKWEJ7c")