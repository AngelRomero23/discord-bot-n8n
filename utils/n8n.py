import aiohttp
from settings.settings import N8N_WEBHOOK_URL

async def enviar_comando_a_n8n(usuario: str, comando: str, canal_id: int) -> None:
    """Envía el comando recibido a n8n vía webhook"""
    payload = {
        "usuario": usuario,
        "comando": comando,
        "canal": canal_id
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(N8N_WEBHOOK_URL, json=payload) as resp:
            if resp.status != 200:
                print(f"Error enviando a n8n: {resp.status}")
