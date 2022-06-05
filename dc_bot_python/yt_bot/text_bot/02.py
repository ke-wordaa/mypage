import discord
import json
from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix='(', intents=intents)
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
async def ping(ctx):
    await ctx.send('%.0fms' %(client.latency*1000))
@client.command()
async def PING(ctx):
    await ctx.send('%.0fms' %(client.latency*1000))

if __name__ == "__main__":
    client.run(jdate['token'])