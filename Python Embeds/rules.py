# python embed for basic discord server rules


@client.command(aliases=['embedrules'])
async def rulesembed(ctx):
  embed=discord.Embed(title="SERVER RULES!", description="GENERAL & CHAT RULES", color=0x00f5d8)    
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/881206826195116124/894205064141492264/Blue_with_Gold_Laurel_Education_Logo__2_-removebg-preview_1.png")
  embed.add_field(name="1. Hate Speech", value="Harassment, hate speech, racism, sexism, absive, and trolling are not allowed here.", inline=False) 
  embed.add_field(name="2. NSFW Content", value="Do not post anything that is NSFW or overly suggestive. If you are unsure if it is considered NSFW or suggestive, you should refrain from posting it.", inline=False) 
  embed.add_field(name="3. Promotion/Trading", value="This server is not a marketplace, do not ask for money, try and buy / sell / giveaway anything.", inline=False) 
  embed.add_field(name="4. Spamming", value="Avoid all forms of spamming – this includes repeated use of bot commands, ALL CAPS or repeatedly mentioning people who are not currently active in the chat.", inline=False) 
  embed.add_field(name="5. Channel Topic", value="Please be mindful of channels and their uses! Useful information about the purpose of each channel can be found in the channel topic or pinned messages.", inline=False) 
  embed.add_field(name="6. Niknames", value="Your nickname/username must comply with the rest of the rules and must be taggable without using any thing like hate speech, nsfw content, etc...", inline=False) 
  embed.add_field(name="7. Commn sense yet Rare", value="Remain civil and considerate towards other users. If there is a conflict, work to defuse it instead of making it worse. If it gets out of hand tag a active mod", inline=False) 
  embed.add_field(name="8. Roles", value="Begging/Asking For Any Role Simultaneously Even If Someone Is Said To Give It To You, This Action Will Result Into A Mute/ban", inline=False) 
  embed.add_field(name="9. Promotion/Marketing", value="Sending Invites, Social Media Links, YouTube Links Or Any Other information Will Result Into A Ban. This Also Includes DM Promotion, Sending Any Of The Above To Any Memer Of The Server Is Also Not Acceptable. Anyone Who Receives Such Kinds Of Dm's, There Is A Very Beautiful Option Called Block, Use It Instead Of Complain In The Server.", inline=False) 
  embed.add_field(name="10. Discord rules and guidlinelines", value="Discord's Terms of Service, Community Guidelines as well as Code of Conduct should be followed by everyone.", inline=False) 
  
  
  await ctx.send(embed=embed)
      
