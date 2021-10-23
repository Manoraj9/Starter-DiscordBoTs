import discord
from discord.ext import commands
import os
import random
import asyncio
import requests
import json

client = commands.Bot(commands.when_mentioned_or("-"))

@client.event
async def on_ready():
  print(' No errors found. {0.user} is ready to play'.format(client))
  print('...............................')

async def ch_pr():
    await client.wait_until_ready()

    statuses = [f"in few servers", "with RajKumar"]

    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(5)


client.loop.create_task(ch_pr())

client.remove_command("help")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('ping'):
    await message.channel.send('pong!')

  if message.content.startswith('Ping'):
    await message.channel.send('pong!')

  if message.content.startswith('Yo'):
    await message.channel.send('Yo!')

  if message.content.startswith('hey'):
    await message.channel.send('Yo!')

  if message.content.startswith('Hey'):
    await message.channel.send('Yo!')

  if message.content.startswith('yo'):
    await message.channel.send('Yo!')

  if message.content.startswith('lol'):
   await message.channel.send('haha')

  if message.content.startswith('Lol'):
   await message.channel.send('haha')

  if message.content.startswith('Wassup '):
   await message.channel.send('Nothing much, jk')

  if message.content.startswith('omg'):
   await message.channel.send('Wah!')

  if message.content.startswith('Omg'):
   await message.channel.send('Wah!')

  if message.content.startswith('Nice'):
   await message.channel.send('Grrreat!')

  if message.content.startswith('Yai'):
   await message.channel.send('Yep')

  if message.content.startswith('Yep'):
   await message.channel.send('Yaa')

  if message.content.startswith('yep'):
   await message.channel.send('Yaa')

  if message.content.startswith('Good'):
   await message.channel.send('Glad to hear that.')

  if message.content.startswith('I am fine'):
   await message.channel.send('Glad to hear that.')

  if message.content.startswith('i am fine'):
   await message.channel.send('Glad to hear that.')

  if message.content.startswith('Who made you'):
   await message.channel.send('I can not tell the exact name of my devloper. Yeah but I know that I am designed by somebody who is in between us.')

  if message.content.startswith('who made you'):
   await message.channel.send('I can not tell the exact name of my devloper. Yeah but I know that I am designed by somebody who is in between us.')

  if message.content.startswith('Who designed you'):
   await message.channel.send('I can not tell the exact name of my devloper. Yeah but I know that I am designed by somebody who is in between us.')

  if message.content.startswith('who designed you'):
   await message.channel.send('I can not tell the exact name of my devloper. Yeah but I know that I am designed by somebody who is in between us.')

  if message.content.startswith('Who programed you'):
   await message.channel.send('I can not tell the exact name of my devloper. Yeah but I know that I am designed by somebody who is in between us.')

  if message.content.startswith('who programed you'):
   await message.channel.send('I can not tell the exact name of my devloper. Yeah but I know that I am designed by somebody who is in between us.')

  if message.content.startswith('Who are you'):
   await message.channel.send('Thats a nice question, well i am a chat bot. Thats it')

  if message.content.startswith('who are you'):
   await message.channel.send('Thats a nice question, well i am a chat bot. Thats it')

  if message.content.startswith('How do you work'):
   await message.channel.send('I keep looking for the questions which i am programed to answer.')

  if message.content.startswith('how do you work'):
   await message.channel.send('I keep looking for the questions which i am programed to answer.')

  if message.content.startswith('What do you do'):
   await message.channel.send('I just keep looking for the questions which i am programed to answer.')

  if message.content.startswith('what do you do'):
   await message.channel.send('I just keep looking for the questions which i am programed to answer.')

  if message.content.startswith('What you do'):
   await message.channel.send('I just keep looking for the questions which i am programed to answer.')

  if message.content.startswith('what you do'):
   await message.channel.send('I just keep looking for the questions which i am programed to answer.')

  if message.content.startswith('Good'):
   await message.channel.send('Glad to hear that.')

  if message.content.startswith('help'):
   await message.channel.send('Yeah, I am here. I was not just gone for a glass of water; Just kidding I am just a chat bot I dont support this command ')

  if message.content.startswith('-help'):
   await message.channel.send('Yeah, I am here. I was not just gone for a glass of water; Just kidding I am just a chat bot I dont support this command ')

token = os.environ['TOKEN']
client.run(token)
