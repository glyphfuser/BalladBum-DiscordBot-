import discord
from discord.ext import commands
import asyncio
import random

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

insults = ["You're slower than a snail carrying a brick!", 
           "If laziness were a sport, you'd come in fourth so you wouldn't have to walk up to the podium.", 
           "Your work ethic would make a sloth look fast."]

@bot.command()
async def track_request(ctx):
    await ctx.send(f"{ctx.message.author.mention} Can you provide a track?")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=1.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send(f"{ctx.message.author.mention} {random.choice(insults)}")
    else:
        await ctx.send(f"Thanks for the track, {ctx.message.author.mention}!")

bot.run
