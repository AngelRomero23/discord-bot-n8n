from discord import Interaction
from discord.ext.commands import Bot
from settings.settings import CANAL_ESPERADOS
from utils.n8n import enviar_comando_a_n8n

async def setup_slash_commands(bot: Bot) -> None:
    """Registra los slash commands para Discord"""

    @bot.tree.command(
        name="get_discounted_price",
        description="Obtén el precio de un producto con descuento de SHEIN"
    )
    async def get_discounted_price(interaction: Interaction) -> None:
        canal_id = interaction.channel.id
        if canal_id not in CANAL_ESPERADOS:
            await interaction.response.send_message(
                "Este comando no está disponible en este canal.",
                ephemeral=True
            )
            return

        # Enviar datos a n8n
        await enviar_comando_a_n8n(interaction.user.name, "precio", canal_id)

        # Respuesta inmediata
        await interaction.response.send_message(
            "Consultando el precio, espera un momento...",
            ephemeral=True
        )
