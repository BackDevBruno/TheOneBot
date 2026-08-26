import discord
from math import ceil


# TO-DO: Remove buttons when content can fit in a single page

class PaginationView(discord.ui.View):
    def __init__(
        self,
        data,
        page_size: int = 5,
        search_text: str | None = None,
    ):
        super().__init__(timeout=60)

        self.data = data
        self.page_size = page_size
        self.search_text = search_text.strip() if search_text else ""
        self.current_page = 0

    @property
    def total_pages(self) -> int:
        return max(ceil(len(self.data) / self.page_size), 1)

    @property
    def page_items(self):
        start = self.current_page * self.page_size
        end = start + self.page_size

        return self.data[start:end]

    def update_buttons(self):
        multiple_pages = self.total_pages > 1

        self.previous_button.disabled = (
            not multiple_pages or self.current_page == 0
        )

        self.next_button.disabled = (
            not multiple_pages or self.current_page == self.total_pages - 1
        )

    def get_embed(self) -> discord.Embed:
        if not self.data:
            title = (
                f"Character '{self.search_text}' not found"
                if self.search_text
                else "No results"
            )

            return discord.Embed(title=title)

        self.update_buttons()

        items = "\n".join(
            f"{index}. {item}"
            for index, item in enumerate(
                self.page_items,
                start=self.current_page * self.page_size + 1,
            )
        )

        title = f"Page {self.current_page + 1}/{self.total_pages}"

        return discord.Embed(
            title=title,
            description=items,
        )

    @discord.ui.button(label="<-", style=discord.ButtonStyle.gray)
    async def previous_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        if self.current_page > 0:
            self.current_page -= 1

        await interaction.response.edit_message(
            embed=self.get_embed(),
            view=self,
        )

    @discord.ui.button(label="->", style=discord.ButtonStyle.gray,)
    async def next_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1

        await interaction.response.edit_message(
            embed=self.get_embed(),
            view=self,
        )