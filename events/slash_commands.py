from discord import Interaction, app_commands
from discord.ext.commands import Bot
from typing import Optional
from settings.settings import CANALES_ESPERADOS
from utils.n8n import enviar_comando_a_n8n

# Lista de productos de ejemplo para el autocomplete
PRODUCTOS_EJEMPLO = ["Bolso", "Camisa", "Zapatos", "Vestido", "Jeans", "Gafas"]

async def setup_slash_commands(bot: Bot):
    @bot.tree.command(
        name="buscar_shein",
        description="Busca un producto en Shein con rango de precios"
    )
    async def buscar_shein(interaction: Interaction, producto: str, min_precio: int, max_precio: int):
        canal_id = interaction.channel.id
        if canal_id not in CANALES_ESPERADOS:
            await interaction.response.send_message(
                "Este comando no está disponible en este canal.",
                ephemeral=True
            )
            return

        # Enviar a n8n usando kwargs
        await enviar_comando_a_n8n(
            usuario=interaction.user.name,
            comando="buscar_shein",
            canal_id=canal_id,
            producto=producto,
            min_precio=min_precio,
            max_precio=max_precio
        )

        await interaction.response.send_message(
            "Consultando el producto en Shein, espera un momento...",
            ephemeral=True
        )

    # Función de autocomplete para el parámetro 'producto'
    @buscar_shein.autocomplete("producto")
    async def autocomplete_producto(
        interaction: Interaction,
        current: str
    ) -> list[app_commands.Choice[str]]:
        # Filtra productos que contengan lo que el usuario escribe
        opciones = [
            app_commands.Choice(name=prod, value=prod)
            for prod in PRODUCTOS_EJEMPLO
            if current.lower() in prod.lower()
        ]
        # Limitar el número de sugerencias a 25 (límite de Discord)
        return opciones[:25]
