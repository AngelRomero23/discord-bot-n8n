from discord import app_commands, Interaction, Client, Object
from settings.settings import CANALES_ESPERADOS, N8N_WEBHOOK_URL
from utils.n8n import enviar_comando_a_n8n

# Coloca aquí el ID de tu servidor de prueba
GUILD_ID = 1419556707935191102  # reemplaza con tu ID real

async def setup_slash_commands(client: Client) -> None:
    """
    Define los comandos slash para que aparezcan como sugerencias en Discord
    de manera inmediata en tu servidor de prueba.
    """

    @client.tree.command(
        name="precio",
        description="Obtén el precio de las camisas",
        guild=Object(id=GUILD_ID)  # <-- esto hace que sea guild command
    )
    async def precio(interaction: Interaction) -> None:
        canal_id: int = interaction.channel.id
        if canal_id not in CANALES_ESPERADOS:
            await interaction.response.send_message(
                "Este comando no está disponible en este canal.",
                ephemeral=True
            )
            return

        # Enviar a n8n para que haga la lógica
        await enviar_comando_a_n8n(interaction.user.name, "precio", canal_id)

        # Respuesta inmediata opcional
        await interaction.response.send_message(
            "Consultando el precio, espera un momento...",
            ephemeral=True
        )