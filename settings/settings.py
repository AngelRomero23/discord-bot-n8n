import os
from dotenv import load_dotenv
from typing import Set

# Cargar variables de entorno
load_dotenv()

DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN", "")
N8N_WEBHOOK_URL: str = os.getenv("N8N_WEBHOOK_URL", "")

# IDs de canales válidos donde se procesarán mensajes
CANALES_ESPERADOS: Set[int] = {
    1422296078278987978
}
