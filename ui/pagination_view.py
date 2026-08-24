import discord
import math


class PaginationView(discord.ui.View):
    def __init__(self, data, page_size=5, search_text=None):
        super().__init__(timeout=60)

        self.data = data
        self.search_text = search_text.strip() if search_text is not None else ""
        self.page_size = page_size

        self.num_pages = max(math.ceil(len(self.data) / self.page_size) - 1, 0)
        self.current_page = 0

    def get_embed(self) -> discord.Embed:
        list_str = ""
        title = ""

        if len(self.data) > 0:
            current_page_size = self.current_page * self.page_size

            list = ""
            if len(self.data) > self.page_size:
                title = f"Page {self.current_page + 1}/{self.num_pages + 1}"
                list = [
                    f"{i + current_page_size}. {c.__str__()}\n" 
                    for i, c in enumerate(
                        self.data[current_page_size : current_page_size + self.page_size],
                        start=1,
                    )
                ]
            else:
                list = [
                    f"{c.__str__()}\n" 
                    for c in self.data[current_page_size : current_page_size + self.page_size]
                ]
            list_str = "\n".join(list)
        else:
            if self.search_text != "":
                title = f"Character '{self.search_text}' not found"
            else:
                title = "No results"

        if self.num_pages == 0:
            for child in self.children:
                if isinstance(child, discord.ui.Button):
                    self.remove_item(child)
        else:
            for child in self.children:
                if isinstance(child, discord.ui.Button):
                    child.disabled = False
                    if ((self.current_page == 0 and child.label == "<-") or
                        (self.current_page == self.num_pages and child.label == "->")):
                        child.disabled = True

        return discord.Embed(title=title, description=list_str)

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
        if self.current_page < self.num_pages:
            self.current_page += 1
        await interaction.response.edit_message(
            embed=self.get_embed(),
            view=self
        )
            
