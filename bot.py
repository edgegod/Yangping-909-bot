import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    channel = bot.get_channel(747716993490354176)
    await channel.send("Hello, world!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}(ms)")

bot.run("NzQ3NzA0MTE0NTAyMzAzODM3.X0SvuA.XaTyeUJgjgEJxIFIS-T77q5cQC8")