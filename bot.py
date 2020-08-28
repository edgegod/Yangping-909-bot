import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    channel = bot.get_channel(747716993490354176)
    await channel.send("Hello, Discord!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}(ms)")

@bot.command()
async def technews(ctx):
    web_data = requests.get('https://buzzorange.com/techorange/')
    soup = BeautifulSoup(web_data.text,"html.parser")
    for news in soup.find(class_='site-main post-listing').findAll(class_='entry-header'):
        await ctx.send(news.find('time').string+':'+news.find('a').string)

bot.run("NzQ3NzA0MTE0NTAyMzAzODM3.X0SvuA.XaTyeUJgjgEJxIFIS-T77q5cQC8")