import discord
import data.cache as cache
import ui.pagination_view as pagination_view

from discord import app_commands
from discord.ext import commands
from typing import Optional


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

@bot.tree.command(name="characters", description="Displays all characters")
@app_commands.describe(name="Character name (optional)")
async def display_characters(
    interaction: discord.Interaction,
    name: Optional[str]
):
    characters = []
    if name is not None and name.strip() != "":
        characters = cache.get_characters_by_name(name)
    else:
        characters = cache.get_characters()

    view = pagination_view.PaginationView(characters)

    await interaction.response.send_message(
        embed=view.get_embed(),
        view=view,
    )
