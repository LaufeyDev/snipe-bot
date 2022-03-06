from aiohttp import ClientRequest
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
bot.sniped_messages = {}

@bot.event
async def on_ready():
    print("Kokushibo is here")

@bot.event
async def on_message_delete(message):
    bot.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@bot.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = bot.sniped_messages[ctx.guild.id]
        
    except:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.channel.send('https://tenor.com/view/kokushi-bo-demon-slayer-kimetsu-no-yaiba-kokushi-bou-kukoshibo-gif-23772122')
    
    await ctx.channel.send("pong!")  



@bot.command()
async def pfp(ctx, *, member: discord.Member=None): 
    if not member: 
        member = ctx.message.author 
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)


@bot.command()
async def Help(ctx):
    embed=discord.Embed(title="Help",  description="Commands so far !ping , !snipe & !pfp.. More will be added soon...", color=0xFF5733)
    await ctx.send(embed=embed)    
    

    





bot.run('Include token')   
