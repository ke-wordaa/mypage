
import os
import discord
import json
from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix='ke.', intents=intents)
with open('set.json','r',encoding='utf8') as jsflie:
    jdate = json.load(jsflie)

@client.event
async def on_ready():
    print(f'{client.user}上線了')
    chinnel = client.get_channel(jdate['chinnel1'])
    await chinnel.send(f"{client.user}上線了")
@client.event
async def on_member_join(member):
    print(f'{member}in')
    chinnel = client.get_channel(jdate['chinnel1'])
    await chinnel.send(f"{member}進來了")
    print("-----------------")
@client.event
async def on_member_remove(member):
    chinnel = client.get_channel(jdate['chinnel1'])
    await chinnel.send(f"{member}退出了")
    print(f'{member}out')
    print("-----------------")
@client.command()
async def load(ctx,extension):
    client.load_extension(f'cmds.{extension}')
    await ctx.send(F'載入{extension}成功')
@client.command()
async def unload(ctx,extension):
    client.unload_extension(F'cmds.{extension}')
    await ctx.send(F'卸載{extension}成功')
@client.command()
async def reload(ctx,extension):
    print(extension)
    client.reload_extension(F'cmds.{extension}')
    await ctx.send(F'重新載入{extension}成功')

for filename in os.listdir('./cmds'):
    print(filename) 
    if filename.endswith('.py'):
        client.load_extension(F"cmds.{filename[:-3]}")
if __name__ == "__main__":
    client.run(jdate['token'])