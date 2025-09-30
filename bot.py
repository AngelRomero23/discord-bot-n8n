# bot.py
import logging
import discord
from discord.ext.commands import Bot
from settings.settings import DISCORD_TOKEN
from events.on_message import manejar_mensaje
from events.slash_commands import setup_slash_commands

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

intents = discord.Intents.default()
intents.message_content = True

bot: Bot = Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready() -> None:
    logging.info(f"Bot conectado como {bot.user}")
    await setup_slash_commands(bot)
    await bot.tree.sync()
    logging.info("Slash commands sincronizados correctamente")

@bot.event
async def on_message(message: discord.Message) -> None:
    await manejar_mensaje(message, bot)

bot.run(DISCORD_TOKEN)

