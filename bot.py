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
    for news in soup.find(class_='site-main post-listing').findAll(class_='entry-header'):
        await ctx.send(news.find('time').string+':'+news.find('a').string)
@bot.event()
async def on_memeber-join{memeber}:
    print(F'{member}litte asshole join!')
    
 @bot.event()
async def on_memeber-remove{memeber}:
    print(F'{member}little asshole leave!')
    
s = input("Please enter the token of the bot:")
bot.run(s)
