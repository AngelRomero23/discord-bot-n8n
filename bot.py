import discord
import os
import aiohttp
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")
N8N_WEBHOOK_URL = os.environ.get("N8N_WEBHOOK_URL")

# IDs de los canales donde el bot debe escuchar mensajes
CANALES_ESPERADOS = [
    1422296078278987978   # Puedes agregar más canales
]

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    # Ignorar mensajes propios
    if message.author == client.user:
        return

    # Filtrar por canales permitidos
    if message.channel.id not in CANALES_ESPERADOS:
        return

    # Preparar payload para n8n
    payload = {
        "usuario": message.author.name,
        "mensaje": message.content,
        "canal": str(message.channel.id)
    }

    # Enviar datos a n8n
    try:
        async with aiohttp.ClientSession() as session:
            await session.post(N8N_WEBHOOK_URL, json=payload)
    except Exception as e:
        print("Error enviando a n8n:", e)

# Ejecutar bot
client.run(TOKEN)
