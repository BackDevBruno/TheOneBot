import discord

from discord import app_commands
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="/",
            intents=intents
        )

    async def setup_hook(self) -> None:
        await self.tree.sync()

bot = Bot()

@bot.tree.command(name="purge", description="Delete recent messages")
@app_commands.describe(amount="Number of messages to delete, default to 1")
async def purge(
    interaction: discord.Interaction,
    amount: app_commands.Range[int, 1, 100],
):
    await interaction.channel.purge(limit=amount) # type: ignore

    await interaction.response.send_message(
        f"Deleted {amount} messages.",
        ephemeral=True
    ) 