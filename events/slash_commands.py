from discord import app_commands, Interaction, Client
from config.config import CANALES_ESPERADOS
from utils.n8n import enviar_comando_a_n8n

async def setup_slash_commands(client: Client) -> None:
    """
    Configura los comandos slash para Discord.
    """

    @client.tree.command(
        name="precio",
        description="Obtén el precio de las camisas"
    )
    async def precio(interaction: Interaction) -> None:
        canal_id: int = interaction.channel.id
        if canal_id not in CANALES_ESPERADOS:
            await interaction.response.send_message(
                "Este comando no está disponible en este canal.",
                ephemeral=True
            )
            return

        # Enviar a n8n para lógica de scraping
        await enviar_comando_a_n8n(interaction.user.name, "precio", canal_id)

        # Respuesta inmediata opcional
        await interaction.response.send_message(
            "Consultando el precio, espera un momento...",
            ephemeral=True
        )
