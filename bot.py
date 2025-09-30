from discord import Interaction, app_commands
from discord.ext.commands import Bot
from typing import Optional
from settings.settings import CANALES_ESPERADOS
from utils.n8n import enviar_comando_a_n8n

# Lista de productos de ejemplo para el autocomplete
PRODUCTOS_EJEMPLO = ["Bolso", "Camisa", "Zapatos", "Vestido", "Jeans", "Gafas"]

async def setup_slash_commands(bot: Bot) -> None:
    """Define los slash commands visibles en Discord con autocomplete."""

    @bot.tree.command(
        name="buscar_shein",
        description="Busca un producto en Shein dentro de un rango de precios"
    )
    @app_commands.describe(
        producto="Nombre del producto a buscar",
        min_precio="Precio mínimo (opcional)",
        max_precio="Precio máximo (opcional)"
    )
    async def buscar_shein(
        interaction: Interaction,
        producto: str,
        min_precio: Optional[int] = 0,
        max_precio: Optional[int] = 1000000
    ) -> None:
        canal_id = interaction.channel.id
        if canal_id not in CANALES_ESPERADOS:
            await interaction.response.send_message(
                "Este comando no está disponible en este canal.",
                ephemeral=True
            )
            return

        await enviar_comando_a_n8n(
            usuario=interaction.user.name,
            comando="buscar_shein",
            canal_id=canal_id,
            producto=producto,
            min_precio=min_precio,
            max_precio=max_precio
        )

        await interaction.response.send_message(
            f"Buscando '{producto}' entre ${min_precio} y ${max_precio}. Por favor espera...",
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