import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">>bot is onlne<<")
    channel = bot.get_channel(801799914635001917)
    await channel.send("Hello, 909!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}(ms)")

@bot.command()
async def technews(ctx):
    web_data = requests.get('https://buzzorange.com/techorange/')
    soup = BeautifulSoup(web_data.text,"html.parser")
    out = ""
    for news in soup.find(class_='site-main post-listing').findAll(class_='entry-header'):
        out += news.find('time').string+':'+news.find('a').string + '\n'
    await ctx.send(out)

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        F'{member}litte asshole join!'
        )

@bot.event
async def on_memeber_remove(memeber):
    await member.create_dm()
    await member.dm_channel.send(
        F'{member}litte asshole leave!'
        )
    
s = input("Please enter the token of the bot:")
bot.run(s)
