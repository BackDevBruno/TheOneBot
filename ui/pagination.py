import discord


class PaginationView(discord.ui.View):
    def __init__(self, pages: list[str]):
        super().__init__(timeout=60)

        self.pages = pages
        self.current_page = 0

    def get_embed(self) -> discord.Embed:
        return discord.Embed(
            title=f"Content — Page {self.current_page + 1}/{len(self.pages)}",
            description=self.pages[self.current_page]
        )

    @discord.ui.button(label="Previous", style=discord.ButtonStyle.gray)
    async def previous(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        if self.current_page > 0:
            self.current_page -= 1

        await interaction.response.edit_message(
            embed=self.get_embed(),
            view=self
        )

    @discord.ui.button(label="Next", style=discord.ButtonStyle.gray)
    async def next(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1

        await interaction.response.edit_message(
            embed=self.get_embed(),
            view=self
        )
