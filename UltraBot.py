import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
import aiohttp
import ctx
import json
import game

HOST = "127.0.0.1"

bot=commands.Bot(command_prefix='!' , pm_help = True , pm_game = True)
dabs='358661627459141642'
start=time.time()

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    await bot.change_presence(game=discord.Game(name='! || In 2 Servers! || Beta Bot || Mad Attack || ',type=1))

@bot.command(pass_context=True)
async def botinfo():
    await bot.say('**__BOT STATS__**')
    await bot.say('__BOT__ : **Streaming**')
    await bot.say('**Updated at  __21/3/2019__**')
    await bot.say('https://discordapp.com/api/oauth2/authorize?client_id=557289829298339841&permissions=8&scope=bot')
    
@bot.command(pass_context=True)
async def mute(ctx,target:discord.Member):
    if ctx.message.author.id==(dabs):
      role=discord.utils.get(ctx.message.server.roles,name='Muted')

      await bot.add_roles(target,role)
    else:
        await bot.say('Sorry Bro No permission!')

@bot.command(pass_context=True)
async def warn(ctx,target:discord.Member):
    if ctx.message.author.id==(dabs):
      await bot.send_message(target,'You Got Warned!!')
    else:
        await bot.say('No permission!')
        
@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member):
    if ctx.message.author.id==(dabs):
      await bot.kick(target)
    else:
        await bot.say('No permission!')

@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
    if ctx.message.author.id==(dabs):
      await bot.ban(target)
    else:
        await bot.say('No permission!')
    
@bot.command(pass_context=True)
async def uptime(ctx):
    now=time.time()
    sec=int(now-start)
    mins=int(sec//60)
    await bot.say(f'Uptime is {sec} seconds!')
 
@bot.command(pass_context=True)
async def clear(ctx,num:int):
    if ctx.message.author.id==(dabs):
        await bot.purge_from(ctx.message.channel,limit=num)
        await bot.say(f'Cleared {num} messages.')
    else:
          await bot.say('No permission!')
          
@bot.command(pass_context=True)
async def game(ctx,text:str,type:int):
    if ctx.message.author.id==(dabs):
        await bot.change_presence(game=discord.Game(name=text,type=type))
    else:
          await bot.say('No permission!')
      
     
bot.run('NTU3Mjg5ODI5Mjk4MzM5ODQx.D3UnQA.GTZHNmk8tpXG76pfCuZ67gFANPE')
