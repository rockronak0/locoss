import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import datetime
import time

bot = commands.Bot(command_prefix="$")
bot.remove_command("help")
BOT_OWNER_ROLE="runner" # change what you need 

@bot.event
async def on_ready():
	while True:
		await bot.change_presence(activity=discord.Activity(type=1,name="Welcome Members!"))
		await asyncio.sleep(5)
		
		await bot.change_presence(activity=discord.Activity(type=1,name="$help"))
		await asyncio.sleep(5)
		
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'''{len(bot.guilds)} servers'''))
		await asyncio.sleep(5)
		print("Online")
	
@bot.event
async def on_member_join(member):
    welcome_channel=get(member.guild.channels, name='welcome')
    embed = discord.Embed(title=f'**__Welcome to {member.guild.name}__**', description=f"**User Name:**\n{member.name}#{member.discriminator}",colour=discord.Colour.green())
    embed.add_field(name="**User ID:**", value=f"{member.id}",inline=True)
    embed.add_field(name="**__Thanks For Joining__**", value=f"{member.name}",inline=True)
    embed.add_field(name="**__Description__**", value="**This Server Is totally free of cost our answer bots are giving answers!**",inline=True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_image(url="http://img1.coolspacetricks.com/images/glittertexts/welcome/090.gif")
    embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939")
    embed.timestamp = datetime.datetime.utcnow()
    await welcome_channel.send(embed=embed)

    dm_msg = "**join our official servers that is giving answers in text and voice study iq is text answer server and best helpers are voice sever join our both servers**\nhttps://discord.gg/VJDd4hP\nhttps://discord.gg/YEDgFkU"
    await member.send(dm_msg)

@bot.command()
async def start(ctx,game:str):
	await ctx.message.delete()
	author = ctx.message.author
	# if BOT_OWNER_ROLE in [role.name for role in author.roles]:
	# 	BOT_OWNER_ROLE="Access"
	if game== 'loco':
		url="https://cdn.discordapp.com/attachments/596710160035217408/597750968528142337/giphy.gif"
	elif game== 'hq':
		url="https://cdn.discordapp.com/attachments/557650994897485834/594847560863186945/IMG_20190426_203610.jpg"
	elif game== 'trivaa':
		url="https://cdn.discordapp.com/attachments/557650994897485834/594847560326447126/IMG_20190426_203621.jpg"
	elif game== 'jeetoh':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594861943454564352/new_mascot_elephant.png"
	elif game== 'karma':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594865537939668992/IMG_20190630_175306_281.JPG"
	elif game== 'confetti':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547395/IMG_20190630_233005_747.JPG"
	elif game== 'swagiq':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547393/IMG_20190630_233031_734.JPG"
	elif game== 'theq':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950648764825600/18vDC_cU_400x400.jpg"
	elif game== 'brainbaazi':
		url="https://is3-ssl.mzstatic.com/image/thumb/Purple118/v4/fc/da/17/fcda17ed-f0b6-6067-ecc4-d9641fed234c/AppIcon-0-1x_U007emarketing-0-0-sRGB-85-220-0-5.png/246x0w.jpg"
	elif game== 'qureka':
		url="https://cdn.discordapp.com/attachments/572922639039856645/595214144060391450/IMG_20190701_165822_749.JPG"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		# BOT_OWNER_ROLE="Access"
		embed = discord.Embed(title='Join Fast :wink:',description='**Game is starting!**',colour=0x98FB98)
		embed.add_field(name='Game', value=f'**{game}**',inline=True)
		embed.set_thumbnail(url=url)
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text=f"Developer By ✞☬Attitude boy☬✞#3939", \
            icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone Game Alert :alarm_clock:",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
        
   

@bot.command()
async def end(ctx,game:str):
	await ctx.message.delete()
	author=ctx.message.author
	if game== 'loco':
		url="https://cdn.discordapp.com/attachments/596710160035217408/597750968528142337/giphy.gif"
	elif game== 'hq':
		url="https://cdn.discordapp.com/attachments/557650994897485834/594847560863186945/IMG_20190426_203610.jpg"
	elif game== 'trivaa':
		url="https://cdn.discordapp.com/attachments/557650994897485834/594847560326447126/IMG_20190426_203621.jpg"
	elif game== 'jeetoh':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594861943454564352/new_mascot_elephant.png"
	elif game== 'karma':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594865537939668992/IMG_20190630_175306_281.JPG"
	elif game== 'confetti':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547395/IMG_20190630_233005_747.JPG"
	elif game== 'swagiq':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547393/IMG_20190630_233031_734.JPG"
	elif game== 'theq':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950648764825600/18vDC_cU_400x400.jpg"
	elif game== 'brainbaazi':
		url="https://is3-ssl.mzstatic.com/image/thumb/Purple118/v4/fc/da/17/fcda17ed-f0b6-6067-ecc4-d9641fed234c/AppIcon-0-1x_U007emarketing-0-0-sRGB-85-220-0-5.png/246x0w.jpg"
	elif game== 'qureka':
		url="https://cdn.discordapp.com/attachments/572922639039856645/595214144060391450/IMG_20190701_165822_749.JPG"  
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed = discord.Embed(title='Game End! :wink:',
                              description='**Game is Ended!**',
                              colour=0x98FB98)
		embed.add_field(name='Game',value=f'**{game}.upper()**',inline=True)
		embed.set_thumbnail(url=url)
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939",icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone :warning:",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
   




@bot.command(name="say",hidden=True)
#@commands.check(fetch)
async def say(ctx, *, content:str):
	author=ctx.message.author
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		await ctx.send(content)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)

@bot.command()
async def invite(ctx):
	#await ctx.send("**__@everyone Add Me to Your servers!__**\n")
	
@bot.command()
async def ping(ctx):
	'''
	This text will be shown in the help command
	'''
	
	# Get the latency of the bot
	latency = bot.latency # Included in the Discord.py library
	await ctx.send(latency)
	
@bot.command()
async def avatar(ctx, user: discord.Member):
	embed=discord.Embed()
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member:discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'''***{member.name}#{member.discriminator} got banned!, Reason={reason}***''')
    await member.send(f'''You were banned from {ctx.message.guild.name},Reason={reason}''')
@ban.error
async def ban_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f'''{ctx.message.author.mention} You can not ban members as you are not having `Ban Members` permission''')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Please pass on all the required arguements\n`$ban @mentionuser reason(if)`')
    if isinstance(error, commands.BadArgument):
        await ctx.send('Member is already banned! or Specify the member perfectly')


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'''***{member.name}#{member.discriminator} got kicked!, Reason={reason}***''')
    await member.send(f'''You were kicked from {ctx.message.guild.name},Reason={reason}''')
@kick.error
async def kick_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f'''{ctx.message.author.mention} You can not kick members as you are not having `Kick Members` permission''')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Please pass on all the required arguements\n`$kick @mentionuser reason(if)`')


@bot.command()
@commands.has_permissions(kick_members = True)
async def warn(ctx,member:discord.Member,*,reason=None):
    await ctx.send(f'''{member.name}#{member.discriminator} got warned!, Reason={reason}''')
    await member.send(f'''You were warned in {ctx.message.guild.name},Reason={reason}''')
@warn.error
async def warn_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f'''{ctx.message.author.mention} You can not warn members as you are not having permission''')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Please pass on all the required arguements\n`$warn @mentionuser reason(if)`')
        
@bot.command(pass_context=True)
async def membercount(ctx):
	embed=discord.Embed(title="**Member Count**", description=f"**No. Of members in this server are {ctx.message.guild.member_count}**",colour=discord.Colour.green())
	await ctx.send(embed=embed)


@bot.command()
async def purge(ctx,amount=1000):
    if 'top' in [i.name for i in ctx.message.author.roles]:
        await ctx.channel.purge(limit=amount+1)

    else:
        await ctx.send('Lol You have no perms')
#brainbaazi
@bot.command(name="brainbaazi",description="")
async def brainbaazi(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" :white_check_mark:"
	else:
		check=" :x:"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Brain Baazi",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple118/v4/fc/da/17/fcda17ed-f0b6-6067-ecc4-d9641fed234c/AppIcon-0-1x_U007emarketing-0-0-sRGB-85-220-0-5.png/246x0w.jpg")
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939",icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
	   
#loco
@bot.command(name="loco",description="")
async def loco(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" :white_check_mark:"
	else:
		check=" :x:"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Loco",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/596710160035217408/597750968528142337/giphy.gif")
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939",icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#hq
@bot.command(name="hq",hidden=True)
async def hq(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" :white_check_mark:"
	else:
		check=" :x:"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="HQ Trivia",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/595173694670635019/SAVE_20190426_203902.gif")
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939",icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
		
#trivaa	
@bot.command(name="trivaa",hidden=True)
async def trivaa(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" :white_check_mark:"
	else:
		check=" :x:"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Trivaa",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/557650994897485834/594847560326447126/IMG_20190426_203621.jpg")
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939",icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#jeetoh
@bot.command(name="jeetoh",hidden=True)
async def jeetoh(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" :white_check_mark:"
	else:
		check=" :x:"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Jeetoh",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/594861943454564352/new_mascot_elephant.png")
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939",icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone",embed=embed)
	else:
		await ctx.send("you not have permisson "+ctx.author.mention)
#karma
@bot.command(name="karma",hidden=True)
async def karma(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" :white_check_mark:"
	else:
		check=" :x:"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="My karma",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/594865537939668992/IMG_20190630_175306_281.JPG")
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939",icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)

#confeeti
@bot.command(name="confetti",hidden=True)
async def confetti(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" :white_check_mark"
	else:
		check=" :x:"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game  Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Confetti-India",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547395/IMG_20190630_233005_747.JPG")
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939",icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#swagiq
@bot.command(name="swagiq",hidden=True)
async def swagiq(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" :white_check_mark:"
	else:
		check=" :x:"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game  Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Swag-IQ",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547393/IMG_20190630_233031_734.JPG")
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939",icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone ",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#the q
@bot.command(name="theq",hidden=True)
async def theq(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" :white_check_mark:"
	else:
		check=" :x:"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game  Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="The-Q",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/594950648764825600/18vDC_cU_400x400.jpg")
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939",icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#qureka
@bot.command(name="qureka",hidden=True)
async def qureka(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" :white_check_mark:"
	else:
		check=" :x:"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game  Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Qureka",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/572922639039856645/595214144060391450/IMG_20190701_165822_749.JPG")
		embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
		embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939",icon_url="https://cdn.discordapp.com/attachments/731757131635621980/737706495726190664/Screenshot_20200723-104510_Google_Play_Store.jpg")
		embed.timestamp = datetime.datetime.utcnow()
		await ctx.send(content="@everyone",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)        


@bot.command(name="help",hidden=True)
async def suggest(ctx):
	embed=discord.Embed(title="**Help Commands**", description="**__$<game_name> <accuracy> <prize_won> <last_question_status> <won/lost>\nExample: $loco 10/10 10₹ correct won__**",colour=discord.Colour.green())
	embed.add_field(name="$say<text>", value="**Use Like That** $say <hii>")
	embed.add_field(name="**__Game Alert__**", value="Use Like This \n1. $start<game_name>\n2. $end<game_name>")
	embed.add_field(name="**Check Ping**", value="$ping")
	embed.add_field(name="**Mod Command!**", value="Use Like That \n1.$ban<mention_member>\n2. $kick<mention_member>\n3. $warn<mention_member>")
	#embed.add_field(name="**Invite Our Bot**", value="**$invite**")
	embed.add_field(name="**Member Count**", value="Use Like That\n $membercount")
	embed.add_field(name="**Clear_Msg**", value="$purge <amount of delete msg>\nUse Like That $purge 1")
	embed.add_field(name="**Avatar**", value="Use Like That \n$avatar <mention_member>")
	embed.set_footer(text="Developer By ✞☬Attitude boy☬✞#3939")
	embed.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=embed)
	
bot.run("NzM3NzIwMTU0NTUyNTMyOTky.XyBdbw.ovM5KTHmbnT4VRIN8l8_ENN13IQ")
