import discord


class PaginationView(discord.ui.View):
    def __init__(self, data):
        super().__init__(timeout=60)

        self.data = data
        self.page_size = 10
        self.current_page = 0

    def get_embed(self) -> discord.Embed:
        return discord.Embed(
            title=f"Page {self.current_page + 1}/{len(self.data)//self.page_size + 1}",
            description="\n".join(["- "+c.__str__() for c in self.data[
                self.current_page * self.page_size : 
                (self.current_page * self.page_size) + self.page_size
            ]])
        )

    @discord.ui.button(label="<-", style=discord.ButtonStyle.gray)
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

    @discord.ui.button(label="->", style=discord.ButtonStyle.gray)
    async def next(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        if self.current_page < len(self.data) - 1:
            self.current_page += 1

        await interaction.response.edit_message(
            embed=self.get_embed(),
            view=self
        )
