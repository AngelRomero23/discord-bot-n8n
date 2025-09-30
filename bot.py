import discord
from discord.ext.commands import Bot
from settings.settings import DISCORD_TOKEN
from events.slash_commands import setup_slash_commands

intents = discord.Intents.default()
intents.message_content = True

bot = Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready() -> None:
    print(f"Bot conectado como {bot.user}")
    await setup_slash_commands(bot)
    await bot.tree.sync()  # Sincroniza los slash commands en Discord
    print("Slash commands sincronizados")

bot.run(DISCORD_TOKEN)
