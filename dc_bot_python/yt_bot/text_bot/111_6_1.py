

import time
from discord.ext import commands
from discord import *
client = Client()
bot = commands.Bot(command_prefix = '(')

@bot.event
async def on_ready():
    print('目前登入身份：', bot.user)
    channel =bot.get_channel(981787663914921994)
    await channel.send(f"{bot.user}上線成功 ")
    await channel.send(f"功能:回覆ip")
@bot.event
#當有訊息時
async def on_message(message):
   
    if 'https://www.youtube' in message.content:
            await message.channel.send("此為youtube影片連結")
    if 'ip' in message.content:
        await message.channel.send(f" 59.102.231.9 版本:1.18.2 ")


bot.run('ODk0MTA3Njg3NTY1MDMzNDgz.GwSZV4.90oskRv7hDeuplt4STpBgoSKp4i29RKXnOuvNU')
