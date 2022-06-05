import json
import random
import discord 
from discord.ext import commands
from asonline.class_es import cog_ess
with open('set.json','r',encoding='utf8') as jsflie:
    jdate = json.load(jsflie)
class reload(cog_ess):
    @commands.command()
    async def 圖片(ctx,self):    
        pic = discord.File(jdate['hi_photo'])
        await ctx.send(file = pic)
     
    @commands.command()
    async def 隨機(ctx,self):    
        re_pic = random.choice(jdate['pic'])
        pic = discord.File(re_pic)
        await ctx.send(file = pic)
def setup(client):
    client.add_cog(reload(client)) 