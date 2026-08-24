import discord
import random
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

@bot.tree.command(name="characters", description="Displays characters from Middle-Earth")
@app_commands.describe(name="Character name")
async def display_characters(
    interaction: discord.Interaction,
    name: Optional[str]
):
    await interaction.response.defer()
    
    characters = []
    if name and name.strip() != "":
        characters = cache.get_characters_by_name(name)
    else:
        characters = cache.get_characters()

    view = pagination_view.PaginationView(characters, search_text=name)

    await interaction.followup.send(
        embed=view.get_embed(),
        view=view,
    )

@bot.tree.command(name="quote", description="Displays a random quote from the LOTR movies")
@app_commands.describe(name="Character name")
async def display_quotes(
    interaction: discord.Interaction,
    name: Optional[str]
):
    await interaction.response.defer()
    
    quotes = []
    if name and name.strip() != "":
        quotes = cache.get_quotes_by_character(name)
    else:
        quotes = cache.get_quotes()

    if quotes:
        random.shuffle(quotes)
        quotes = [quotes[0]]

    view = pagination_view.PaginationView(quotes, search_text=name)

    await interaction.followup.send(
        embed=view.get_embed(),
        view=view,
    )