# basic embed of the featuring bot's commands

  
@client.command(aliases=['cmd'])
async def commands(ctx):
   embed=discord.Embed(title="Commands!", description="All commands are listed here. To use them first type the prefix `*` ", color=0x00f5d8) 
   embed.set_author(name="RajKumar Bot v3.4", icon_url="https://media.discordapp.net/attachments/864037132409241610/897340007411490856/M.png")
   embed.set_thumbnail(url="https://media.discordapp.net/attachments/881206826195116124/894205064141492264/Blue_with_Gold_Laurel_Education_Logo__2_-removebg-preview_1.png")
   embed.add_field(name=":8ball: 8ball", value="Give it a try, type ``*tell`` and then your question.'", inline=True) 
   embed.add_field(name=":camera: Avatar", value="`*av` Shows your/member's avatar.", inline=True)
   embed.add_field(name=":person_tipping_hand: Info", value="`*Info member` Shows some Information about the spesefic member.", inline=True)
   embed.add_field(name=":game_die: Dice", value="`*roll` Rolls a random number between 1 to 6.", inline=True)
   embed.add_field(name=":grin: Meme", value="`*meme` Sends a random meme video/image.", inline=True)
   embed.add_field(name=":dog: Dog", value="`*bark` Shows a random dog image.", inline=True)
   embed.add_field(name=":cat: Cat", value="`*cat` Shows a random cat image.", inline=True)
   embed.set_footer(text=f'Commands requested by {ctx.author}') 
  
   await ctx.send(embed=embed)
