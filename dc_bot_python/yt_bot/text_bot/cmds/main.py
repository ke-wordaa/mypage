
from discord.ext import commands
from asonline.class_es import cog_ess

class main(cog_ess):
    @commands.command()
    async def ping(self,ctx):
        await ctx.send('%.0fms' %(self.client.latency*1000))
    @commands.command()
    async def PING(self,ctx):
        await ctx.send('%.0fms' %(self.client.latency*1000))   
def setup(client):
    client.add_cog(main(client)) 