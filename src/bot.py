import nextcord
from dotenv import load_dotenv, find_dotenv
import asyncio
import random
import os
from nextcord.ext import commands

load_dotenv(find_dotenv())

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

description = "my bot"
intents = nextcord.Intents.default()
intents.message_content, intents.members = True, True

bot = commands.Bot(
    command_prefix="!", description=description, intents=intents
)


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong")


@bot.command()
async def scan(ctx):
    msg = "The list of all online members are:\n```"

    for member in ctx.guild.members:
        if member.status == nextcord.Status.online:
            msg += str(member) + "\n"
    msg += "```"
    await ctx.send(msg)


bot.run(TOKEN)
