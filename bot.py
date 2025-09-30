# bot.py
import discord
from discord.ext import commands
from settings.settings import DISCORD_TOKEN
from events.on_message import manejar_mensaje
from events.slash_commands import setup_slash_commands

intents = discord.Intents.default()
intents.message_content = True  # Necesario para on_message

# Usamos commands.Bot para tener slash commands
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready() -> None:
    print(f"Bot conectado como {bot.user}")
    await setup_slash_commands(bot)  # Configura los slash commands
    await bot.tree.sync()  # Sincroniza con Discord

@bot.event
async def on_message(message: discord.Message) -> None:
    await manejar_mensaje(message, bot)

bot.run(DISCORD_TOKEN)
