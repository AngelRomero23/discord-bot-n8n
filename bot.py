import discord
from discord import Client
from .config.config import DISCORD_TOKEN
from events.on_message import manejar_mensaje
from events.slash_commands import setup_slash_commands

intents = discord.Intents.default()
intents.message_content = True
client: Client = discord.Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f"Bot conectado como {client.user}")
    await setup_slash_commands(client)
    await client.tree.sync()  # Sincroniza los slash commands

@client.event
async def on_message(message: discord.Message) -> None:
    await manejar_mensaje(message, client)

client.run(DISCORD_TOKEN)
