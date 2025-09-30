# utils/n8n.py
import aiohttp
import logging
from settings.settings import N8N_WEBHOOK_URL
from typing import Any

logger = logging.getLogger("n8n")
logger.setLevel(logging.INFO)  # o DEBUG si quieres más detalle

async def enviar_comando_a_n8n(usuario: str, comando: str, canal_id: int, **kwargs: Any) -> None:
    """
    Envía un comando a n8n vía webhook.
    Permite pasar parámetros adicionales como kwargs (producto, min_precio, max_precio, etc.).
    """
    payload = {
        "usuario": usuario,
        "comando": comando,
        "canal_id": canal_id,
        **kwargs
    }

    logger.info(f"Enviando comando a n8n: {payload}")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(N8N_WEBHOOK_URL, json=payload) as resp:
                if resp.status != 200:
                    texto = await resp.text()
                    logger.error(f"Falló enviar a n8n: {resp.status} - {texto}")
                else:
                    logger.info(f"Comando enviado correctamente a n8n: {comando}")
    except Exception as e:
        logger.exception(f"Error enviando comando a n8n: {e}")
