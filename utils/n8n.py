import aiohttp
from settings.settings import N8N_WEBHOOK_URL

async def enviar_comando_a_n8n(**kwargs) -> None:
    """Envía el comando recibido a n8n vía webhook"""
    payload = {
        **kwargs
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(N8N_WEBHOOK_URL, json=payload) as resp:
            if resp.status != 200:
                print(f"Error enviando a n8n: {resp.status}")
