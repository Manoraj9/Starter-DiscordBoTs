# Help command embed in python


@client.command(aliases=['h'])
async def help( ctx):
   embed=discord.Embed(title="Help!", description="Hi there, its me RajKumar in a complete new style.", color=0x00f5d8) 
   embed.set_author(name="RajKumar Bot v4.2 ", icon_url="https://media.discordapp.net/attachments/881206826195116124/894205064141492264/Blue_with_Gold_Laurel_Education_Logo__2_-removebg-preview_1.png")
   embed.set_thumbnail(url="https://media.discordapp.net/attachments/864037132409241610/897340007411490856/M.png")
   embed.add_field(name=":video_game: Commands", value="Wanna see the full list of commands. Give it a try; you can type `*commands` to see the full list of commands.", inline=False) 
   embed.add_field(name=":red_car: About", value="The new verson4.2 has came with many new more fun commands, I hope you will love it. Note I am now under devlopment so if you see any bug you can report or give the feedback to me devloper Manoraj and donot worry is any of my cmd is not working you can give the feedback to my devloper.", inline=True)
   embed.set_footer(text=f'Requested by {ctx.author}')
  
   await ctx.send(embed=embed)
  
