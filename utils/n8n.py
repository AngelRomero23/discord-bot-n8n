import aiohttp
import os

async def enviar_comando_a_n8n(usuario: str, comando: str, canal: int) -> None:
    """
    Envía la ejecución de un comando a n8n vía webhook.
    """
    payload = {
        "usuario": usuario,
        "comando": comando,
        "canal": str(canal)
    }
    try:
        async with aiohttp.ClientSession() as session:
            await session.post(
                url=os.environ.get("N8N_WEBHOOK_URL"),
                json=payload
            )
    except Exception as e:
        print("Error enviando comando a n8n:", e)
