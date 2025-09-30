from discord import Interaction
from discord.ext.commands import Bot
from settings.settings import CANALES_ESPERADOS
from utils.n8n import enviar_comando_a_n8n

async def setup_slash_commands(bot: Bot) -> None:
    """Define los slash commands visibles en Discord."""

    @bot.tree.command(
        name="precio",
        description="Obtén el precio de las camisas"
    )
    async def precio(interaction: Interaction) -> None:
        canal_id = interaction.channel.id
        if canal_id not in CANALES_ESPERADOS:
            await interaction.response.send_message(
                "Este comando no está disponible en este canal.",
                ephemeral=True
            )
            return

        await enviar_comando_a_n8n(interaction.user.name, "precio", canal_id)

        await interaction.response.send_message(
            "Consultando el precio, espera un momento...",
            ephemeral=True
        )
