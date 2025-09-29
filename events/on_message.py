from discord import Message, Client
from utils.n8n import enviar_comando_a_n8n
from config.config import CANALES_ESPERADOS

async def manejar_mensaje(message: Message, client: Client) -> None:
    """
    Maneja mensajes normales (no slash commands).
    """
    if message.author == client.user:
        return

    canal_id: int = message.channel.id
    if canal_id not in CANALES_ESPERADOS:
        return

    # Enviar mensaje a n8n para procesar
    await enviar_comando_a_n8n(message.author.name, message.content, canal_id)
