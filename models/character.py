from pydantic import BaseModel, Field


class Character(BaseModel):
    id: str = Field(alias="_id")
    name: str
    wiki_url: str | None = Field(alias="wikiUrl", default=None)
    race: str | None = None
    birth: str | None = None
    gender: str | None = None
    death: str | None = None
    hair: str | None = None
    height: str | None = None
    realm: str | None = None
    spouse: str | None = None

    def __str__(self) -> str:
        return (
            f"**{self.name}**\n"+
            f"Race: {self.race or "Unknown"}\n"+
            f"Gender: {self.gender or "Unknown"}\n"
            f"Birth: {self.birth or "Unknown"}\n"
            f"Death: {self.death or "Unknown"}\n"
            f"Realm: {self.realm or "Unknown"}\n"
            f"Spouse: {self.spouse or "Unknown"}"
        )